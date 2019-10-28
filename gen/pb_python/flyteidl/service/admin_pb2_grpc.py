# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2
from flyteidl.admin import event_pb2 as flyteidl_dot_admin_dot_event__pb2
from flyteidl.admin import execution_pb2 as flyteidl_dot_admin_dot_execution__pb2
from flyteidl.admin import launch_plan_pb2 as flyteidl_dot_admin_dot_launch__plan__pb2
from flyteidl.admin import node_execution_pb2 as flyteidl_dot_admin_dot_node__execution__pb2
from flyteidl.admin import project_domain_attributes_pb2 as flyteidl_dot_admin_dot_project__domain__attributes__pb2
from flyteidl.admin import project_pb2 as flyteidl_dot_admin_dot_project__pb2
from flyteidl.admin import task_execution_pb2 as flyteidl_dot_admin_dot_task__execution__pb2
from flyteidl.admin import task_pb2 as flyteidl_dot_admin_dot_task__pb2
from flyteidl.admin import workflow_pb2 as flyteidl_dot_admin_dot_workflow__pb2


class AdminServiceStub(object):
  """The following defines an RPC service that is also served over HTTP via grpc-gateway.
  Standard response codes for both are defined here: https://github.com/grpc-ecosystem/grpc-gateway/blob/master/runtime/errors.go
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateTask = channel.unary_unary(
        '/flyteidl.service.AdminService/CreateTask',
        request_serializer=flyteidl_dot_admin_dot_task__pb2.TaskCreateRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_task__pb2.TaskCreateResponse.FromString,
        )
    self.GetTask = channel.unary_unary(
        '/flyteidl.service.AdminService/GetTask',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.ObjectGetRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_task__pb2.Task.FromString,
        )
    self.ListTaskIds = channel.unary_unary(
        '/flyteidl.service.AdminService/ListTaskIds',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierList.FromString,
        )
    self.ListTasks = channel.unary_unary(
        '/flyteidl.service.AdminService/ListTasks',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.ResourceListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_task__pb2.TaskList.FromString,
        )
    self.CreateWorkflow = channel.unary_unary(
        '/flyteidl.service.AdminService/CreateWorkflow',
        request_serializer=flyteidl_dot_admin_dot_workflow__pb2.WorkflowCreateRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_workflow__pb2.WorkflowCreateResponse.FromString,
        )
    self.GetWorkflow = channel.unary_unary(
        '/flyteidl.service.AdminService/GetWorkflow',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.ObjectGetRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_workflow__pb2.Workflow.FromString,
        )
    self.ListWorkflowIds = channel.unary_unary(
        '/flyteidl.service.AdminService/ListWorkflowIds',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierList.FromString,
        )
    self.ListWorkflows = channel.unary_unary(
        '/flyteidl.service.AdminService/ListWorkflows',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.ResourceListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_workflow__pb2.WorkflowList.FromString,
        )
    self.CreateLaunchPlan = channel.unary_unary(
        '/flyteidl.service.AdminService/CreateLaunchPlan',
        request_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanCreateRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanCreateResponse.FromString,
        )
    self.GetLaunchPlan = channel.unary_unary(
        '/flyteidl.service.AdminService/GetLaunchPlan',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.ObjectGetRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlan.FromString,
        )
    self.GetActiveLaunchPlan = channel.unary_unary(
        '/flyteidl.service.AdminService/GetActiveLaunchPlan',
        request_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.ActiveLaunchPlanRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlan.FromString,
        )
    self.ListActiveLaunchPlans = channel.unary_unary(
        '/flyteidl.service.AdminService/ListActiveLaunchPlans',
        request_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.ActiveLaunchPlanListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanList.FromString,
        )
    self.ListLaunchPlanIds = channel.unary_unary(
        '/flyteidl.service.AdminService/ListLaunchPlanIds',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierList.FromString,
        )
    self.ListLaunchPlans = channel.unary_unary(
        '/flyteidl.service.AdminService/ListLaunchPlans',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.ResourceListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanList.FromString,
        )
    self.UpdateLaunchPlan = channel.unary_unary(
        '/flyteidl.service.AdminService/UpdateLaunchPlan',
        request_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanUpdateRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanUpdateResponse.FromString,
        )
    self.CreateExecution = channel.unary_unary(
        '/flyteidl.service.AdminService/CreateExecution',
        request_serializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionCreateRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionCreateResponse.FromString,
        )
    self.RelaunchExecution = channel.unary_unary(
        '/flyteidl.service.AdminService/RelaunchExecution',
        request_serializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionRelaunchRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionCreateResponse.FromString,
        )
    self.GetExecution = channel.unary_unary(
        '/flyteidl.service.AdminService/GetExecution',
        request_serializer=flyteidl_dot_admin_dot_execution__pb2.WorkflowExecutionGetRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_execution__pb2.Execution.FromString,
        )
    self.GetExecutionData = channel.unary_unary(
        '/flyteidl.service.AdminService/GetExecutionData',
        request_serializer=flyteidl_dot_admin_dot_execution__pb2.WorkflowExecutionGetDataRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_execution__pb2.WorkflowExecutionGetDataResponse.FromString,
        )
    self.ListExecutions = channel.unary_unary(
        '/flyteidl.service.AdminService/ListExecutions',
        request_serializer=flyteidl_dot_admin_dot_common__pb2.ResourceListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionList.FromString,
        )
    self.TerminateExecution = channel.unary_unary(
        '/flyteidl.service.AdminService/TerminateExecution',
        request_serializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionTerminateRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionTerminateResponse.FromString,
        )
    self.GetNodeExecution = channel.unary_unary(
        '/flyteidl.service.AdminService/GetNodeExecution',
        request_serializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionGetRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecution.FromString,
        )
    self.ListNodeExecutions = channel.unary_unary(
        '/flyteidl.service.AdminService/ListNodeExecutions',
        request_serializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionList.FromString,
        )
    self.ListNodeExecutionsForTask = channel.unary_unary(
        '/flyteidl.service.AdminService/ListNodeExecutionsForTask',
        request_serializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionForTaskListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionList.FromString,
        )
    self.GetNodeExecutionData = channel.unary_unary(
        '/flyteidl.service.AdminService/GetNodeExecutionData',
        request_serializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionGetDataRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionGetDataResponse.FromString,
        )
    self.RegisterProject = channel.unary_unary(
        '/flyteidl.service.AdminService/RegisterProject',
        request_serializer=flyteidl_dot_admin_dot_project__pb2.ProjectRegisterRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_project__pb2.ProjectRegisterResponse.FromString,
        )
    self.ListProjects = channel.unary_unary(
        '/flyteidl.service.AdminService/ListProjects',
        request_serializer=flyteidl_dot_admin_dot_project__pb2.ProjectListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_project__pb2.Projects.FromString,
        )
    self.CreateWorkflowEvent = channel.unary_unary(
        '/flyteidl.service.AdminService/CreateWorkflowEvent',
        request_serializer=flyteidl_dot_admin_dot_event__pb2.WorkflowExecutionEventRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_event__pb2.WorkflowExecutionEventResponse.FromString,
        )
    self.CreateNodeEvent = channel.unary_unary(
        '/flyteidl.service.AdminService/CreateNodeEvent',
        request_serializer=flyteidl_dot_admin_dot_event__pb2.NodeExecutionEventRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_event__pb2.NodeExecutionEventResponse.FromString,
        )
    self.CreateTaskEvent = channel.unary_unary(
        '/flyteidl.service.AdminService/CreateTaskEvent',
        request_serializer=flyteidl_dot_admin_dot_event__pb2.TaskExecutionEventRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_event__pb2.TaskExecutionEventResponse.FromString,
        )
    self.GetTaskExecution = channel.unary_unary(
        '/flyteidl.service.AdminService/GetTaskExecution',
        request_serializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionGetRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecution.FromString,
        )
    self.ListTaskExecutions = channel.unary_unary(
        '/flyteidl.service.AdminService/ListTaskExecutions',
        request_serializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionListRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionList.FromString,
        )
    self.GetTaskExecutionData = channel.unary_unary(
        '/flyteidl.service.AdminService/GetTaskExecutionData',
        request_serializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionGetDataRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionGetDataResponse.FromString,
        )
    self.UpdateProjectDomainAttributes = channel.unary_unary(
        '/flyteidl.service.AdminService/UpdateProjectDomainAttributes',
        request_serializer=flyteidl_dot_admin_dot_project__domain__attributes__pb2.ProjectDomainAttributesUpdateRequest.SerializeToString,
        response_deserializer=flyteidl_dot_admin_dot_project__domain__attributes__pb2.ProjectDomainAttributesUpdateResponse.FromString,
        )


class AdminServiceServicer(object):
  """The following defines an RPC service that is also served over HTTP via grpc-gateway.
  Standard response codes for both are defined here: https://github.com/grpc-ecosystem/grpc-gateway/blob/master/runtime/errors.go
  """

  def CreateTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTaskIds(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateWorkflow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWorkflow(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListWorkflowIds(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListWorkflows(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateLaunchPlan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLaunchPlan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetActiveLaunchPlan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListActiveLaunchPlans(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListLaunchPlanIds(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListLaunchPlans(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLaunchPlan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateExecution(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RelaunchExecution(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExecution(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExecutionData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListExecutions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TerminateExecution(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNodeExecution(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListNodeExecutions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListNodeExecutionsForTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNodeExecutionData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterProject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListProjects(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateWorkflowEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateNodeEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTaskEvent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTaskExecution(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTaskExecutions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTaskExecutionData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateProjectDomainAttributes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdminServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateTask': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTask,
          request_deserializer=flyteidl_dot_admin_dot_task__pb2.TaskCreateRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_task__pb2.TaskCreateResponse.SerializeToString,
      ),
      'GetTask': grpc.unary_unary_rpc_method_handler(
          servicer.GetTask,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.ObjectGetRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_task__pb2.Task.SerializeToString,
      ),
      'ListTaskIds': grpc.unary_unary_rpc_method_handler(
          servicer.ListTaskIds,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierList.SerializeToString,
      ),
      'ListTasks': grpc.unary_unary_rpc_method_handler(
          servicer.ListTasks,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.ResourceListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_task__pb2.TaskList.SerializeToString,
      ),
      'CreateWorkflow': grpc.unary_unary_rpc_method_handler(
          servicer.CreateWorkflow,
          request_deserializer=flyteidl_dot_admin_dot_workflow__pb2.WorkflowCreateRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_workflow__pb2.WorkflowCreateResponse.SerializeToString,
      ),
      'GetWorkflow': grpc.unary_unary_rpc_method_handler(
          servicer.GetWorkflow,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.ObjectGetRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_workflow__pb2.Workflow.SerializeToString,
      ),
      'ListWorkflowIds': grpc.unary_unary_rpc_method_handler(
          servicer.ListWorkflowIds,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierList.SerializeToString,
      ),
      'ListWorkflows': grpc.unary_unary_rpc_method_handler(
          servicer.ListWorkflows,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.ResourceListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_workflow__pb2.WorkflowList.SerializeToString,
      ),
      'CreateLaunchPlan': grpc.unary_unary_rpc_method_handler(
          servicer.CreateLaunchPlan,
          request_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanCreateRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanCreateResponse.SerializeToString,
      ),
      'GetLaunchPlan': grpc.unary_unary_rpc_method_handler(
          servicer.GetLaunchPlan,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.ObjectGetRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlan.SerializeToString,
      ),
      'GetActiveLaunchPlan': grpc.unary_unary_rpc_method_handler(
          servicer.GetActiveLaunchPlan,
          request_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.ActiveLaunchPlanRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlan.SerializeToString,
      ),
      'ListActiveLaunchPlans': grpc.unary_unary_rpc_method_handler(
          servicer.ListActiveLaunchPlans,
          request_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.ActiveLaunchPlanListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanList.SerializeToString,
      ),
      'ListLaunchPlanIds': grpc.unary_unary_rpc_method_handler(
          servicer.ListLaunchPlanIds,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_common__pb2.NamedEntityIdentifierList.SerializeToString,
      ),
      'ListLaunchPlans': grpc.unary_unary_rpc_method_handler(
          servicer.ListLaunchPlans,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.ResourceListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanList.SerializeToString,
      ),
      'UpdateLaunchPlan': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLaunchPlan,
          request_deserializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanUpdateRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_launch__plan__pb2.LaunchPlanUpdateResponse.SerializeToString,
      ),
      'CreateExecution': grpc.unary_unary_rpc_method_handler(
          servicer.CreateExecution,
          request_deserializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionCreateRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionCreateResponse.SerializeToString,
      ),
      'RelaunchExecution': grpc.unary_unary_rpc_method_handler(
          servicer.RelaunchExecution,
          request_deserializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionRelaunchRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionCreateResponse.SerializeToString,
      ),
      'GetExecution': grpc.unary_unary_rpc_method_handler(
          servicer.GetExecution,
          request_deserializer=flyteidl_dot_admin_dot_execution__pb2.WorkflowExecutionGetRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_execution__pb2.Execution.SerializeToString,
      ),
      'GetExecutionData': grpc.unary_unary_rpc_method_handler(
          servicer.GetExecutionData,
          request_deserializer=flyteidl_dot_admin_dot_execution__pb2.WorkflowExecutionGetDataRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_execution__pb2.WorkflowExecutionGetDataResponse.SerializeToString,
      ),
      'ListExecutions': grpc.unary_unary_rpc_method_handler(
          servicer.ListExecutions,
          request_deserializer=flyteidl_dot_admin_dot_common__pb2.ResourceListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionList.SerializeToString,
      ),
      'TerminateExecution': grpc.unary_unary_rpc_method_handler(
          servicer.TerminateExecution,
          request_deserializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionTerminateRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_execution__pb2.ExecutionTerminateResponse.SerializeToString,
      ),
      'GetNodeExecution': grpc.unary_unary_rpc_method_handler(
          servicer.GetNodeExecution,
          request_deserializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionGetRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecution.SerializeToString,
      ),
      'ListNodeExecutions': grpc.unary_unary_rpc_method_handler(
          servicer.ListNodeExecutions,
          request_deserializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionList.SerializeToString,
      ),
      'ListNodeExecutionsForTask': grpc.unary_unary_rpc_method_handler(
          servicer.ListNodeExecutionsForTask,
          request_deserializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionForTaskListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionList.SerializeToString,
      ),
      'GetNodeExecutionData': grpc.unary_unary_rpc_method_handler(
          servicer.GetNodeExecutionData,
          request_deserializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionGetDataRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_node__execution__pb2.NodeExecutionGetDataResponse.SerializeToString,
      ),
      'RegisterProject': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterProject,
          request_deserializer=flyteidl_dot_admin_dot_project__pb2.ProjectRegisterRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_project__pb2.ProjectRegisterResponse.SerializeToString,
      ),
      'ListProjects': grpc.unary_unary_rpc_method_handler(
          servicer.ListProjects,
          request_deserializer=flyteidl_dot_admin_dot_project__pb2.ProjectListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_project__pb2.Projects.SerializeToString,
      ),
      'CreateWorkflowEvent': grpc.unary_unary_rpc_method_handler(
          servicer.CreateWorkflowEvent,
          request_deserializer=flyteidl_dot_admin_dot_event__pb2.WorkflowExecutionEventRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_event__pb2.WorkflowExecutionEventResponse.SerializeToString,
      ),
      'CreateNodeEvent': grpc.unary_unary_rpc_method_handler(
          servicer.CreateNodeEvent,
          request_deserializer=flyteidl_dot_admin_dot_event__pb2.NodeExecutionEventRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_event__pb2.NodeExecutionEventResponse.SerializeToString,
      ),
      'CreateTaskEvent': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTaskEvent,
          request_deserializer=flyteidl_dot_admin_dot_event__pb2.TaskExecutionEventRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_event__pb2.TaskExecutionEventResponse.SerializeToString,
      ),
      'GetTaskExecution': grpc.unary_unary_rpc_method_handler(
          servicer.GetTaskExecution,
          request_deserializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionGetRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecution.SerializeToString,
      ),
      'ListTaskExecutions': grpc.unary_unary_rpc_method_handler(
          servicer.ListTaskExecutions,
          request_deserializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionListRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionList.SerializeToString,
      ),
      'GetTaskExecutionData': grpc.unary_unary_rpc_method_handler(
          servicer.GetTaskExecutionData,
          request_deserializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionGetDataRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_task__execution__pb2.TaskExecutionGetDataResponse.SerializeToString,
      ),
      'UpdateProjectDomainAttributes': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateProjectDomainAttributes,
          request_deserializer=flyteidl_dot_admin_dot_project__domain__attributes__pb2.ProjectDomainAttributesUpdateRequest.FromString,
          response_serializer=flyteidl_dot_admin_dot_project__domain__attributes__pb2.ProjectDomainAttributesUpdateResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'flyteidl.service.AdminService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
