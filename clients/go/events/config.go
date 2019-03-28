package events

import (
	"context"

	"github.com/lyft/flytestdlib/config"
	"github.com/lyft/flytestdlib/logger"
)

//go:generate pflags Config

type EventReportingType = string

// The reserved config section key for storage.
const configSectionKey = "Event"

const (
	EventSinkLog   EventReportingType = "log"
	EventSinkFile  EventReportingType = "file"
	EventSinkAdmin EventReportingType = "admin"
)

var (
	configSection = config.MustRegisterSection(configSectionKey, &Config{})
)

type Config struct {
	Type     EventReportingType `json:"type" pflag:",Sets the type of EventSink to configure [log/admin/file]."`
	FilePath string             `json:"file-path" pflag:",For file types, specify where the file should be located."`
	Rate     int64              `json:"rate" pflag:"int64(500),Max rate at which events can be recorded per second."`
	Capacity int                `json:"capacity" pflag:"1000,The max bucket size for event recording tokens."`
}

// Retrieve current global config for storage.
func GetConfig(ctx context.Context) *Config {
	if c, ok := configSection.GetConfig().(*Config); ok {
		return c
	}

	logger.Warnf(ctx, "Failed to retrieve config section [%v].", configSectionKey)
	return nil
}
