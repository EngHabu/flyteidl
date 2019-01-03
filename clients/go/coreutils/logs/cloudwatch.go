package logs

import (
	"fmt"
	"github.com/lyft/flyteidl/gen/pb-go/flyteidl/core"
	"strings"
)

type cloudwatchLogPlugin struct {
	region    string
	groupName string
}

func (s cloudwatchLogPlugin) GetTaskLog(podName, namespace, containerName, containerId, logName string) (core.TaskLog, error) {

	// Container IDs are prefixed with docker://, cri-o://, etc. which is stripped by fluentd before pushing to a log
	// stream.  Therefore, we must also strip the prefix.
	// Also, container names are
	stripDelimiter := "://"
	if split := strings.Split(containerId, stripDelimiter); len(split) > 1 {
		containerId = split[1]
	}

	return core.TaskLog{
		Uri: fmt.Sprintf(
			"https://console.aws.amazon.com/cloudwatch/home?region=%s#logEventViewer:group=%s;stream=var.log.containers.%s_%s_%s-%s.log",
			s.region,
			s.groupName,
			podName,
			namespace,
			containerName,
			containerId),
		Name:          logName,
		MessageFormat: core.TaskLog_JSON,
	}, nil
}

func NewCloudwatchLogPlugin(region, groupName string) LogPlugin {
	return &cloudwatchLogPlugin{
		region:    region,
		groupName: groupName,
	}
}
