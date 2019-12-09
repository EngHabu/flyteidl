#!/bin/bash
set -e
set -x
which mockery || (GO111MODULE=off go install github.com/vektra/mockery/cmd/mockery)

mockery -dir=gen/pb-go/flyteidl/service/ -name=AdminServiceClient -output=clients/go/admin/mocks
mockery -dir=gen/pb-go/flyteidl/datacatalog/ -name=ArtifactsClient -output=clients/go/datacatalog/mocks
