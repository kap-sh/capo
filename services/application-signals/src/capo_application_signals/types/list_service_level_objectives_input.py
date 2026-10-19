"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceLevelObjectivesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attributes
    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.dependency_config
    import capo_application_signals.types.list_service_level_objectives_max_results
    import capo_application_signals.types.metric_source
    import capo_application_signals.types.metric_source_types
    import capo_application_signals.types.next_token
    import capo_application_signals.types.operation_name


class ListServiceLevelObjectivesInput(TypedDict, closed=True):
    key_attributes: NotRequired["capo_application_signals.types.attributes.Attributes"]
    """<p>You can use this optional field to specify which services you want to retrieve SLO information for.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>"""
    operation_name: NotRequired[
        "capo_application_signals.types.operation_name.OperationName"
    ]
    """<p>The name of the operation that this SLO is associated with.</p>"""
    dependency_config: NotRequired[
        "capo_application_signals.types.dependency_config.DependencyConfig"
    ]
    """<p>Identifies the dependency using the <code>DependencyKeyAttributes</code> and <code>DependencyOperationName</code>. </p>"""
    max_results: NotRequired[
        "capo_application_signals.types.list_service_level_objectives_max_results.ListServiceLevelObjectivesMaxResults"
    ]
    """<p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives.</p>"""
    metric_source_types: NotRequired[
        "capo_application_signals.types.metric_source_types.MetricSourceTypes"
    ]
    """<p>Use this optional field to only include SLOs with the specified metric source types in the output. Supported types are:</p> <ul> <li> <p>Service operation</p> </li> <li> <p>Service dependency</p> </li> <li> <p>Service</p> </li> <li> <p>CloudWatch metric</p> </li> <li> <p>AppMonitor</p> </li> <li> <p>Canary</p> </li> </ul>"""
    include_linked_accounts: NotRequired["bool"]
    """<p>If you are using this operation in a monitoring account, specify <code>true</code> to include SLO from source accounts in the returned data. </p> <p>When you are monitoring an account, you can use Amazon Web Services account ID in <code>KeyAttribute</code> filter for service source account and <code>SloOwnerawsaccountID</code> for SLO source account with <code>IncludeLinkedAccounts</code> to filter the returned data to only a single source account. </p>"""
    slo_owner_aws_account_id: NotRequired[
        "capo_application_signals.types.aws_account_id.AwsAccountId"
    ]
    """<p>SLO's Amazon Web Services account ID.</p>"""
    metric_source: NotRequired[
        "capo_application_signals.types.metric_source.MetricSource"
    ]
    """<p>Identifies the metric source to filter SLOs by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceLevelObjectivesInput) -> dict:
    out: dict = {}
    if "key_attributes" in value:
        import capo_application_signals.types.attributes

        out["KeyAttributes"] = capo_application_signals.types.attributes.serialize_json(
            value["key_attributes"]
        )
    if "dependency_config" in value:
        import capo_application_signals.types.dependency_config

        out["DependencyConfig"] = (
            capo_application_signals.types.dependency_config.serialize_json(
                value["dependency_config"]
            )
        )
    if "metric_source_types" in value:
        import capo_application_signals.types.metric_source_types

        out["MetricSourceTypes"] = (
            capo_application_signals.types.metric_source_types.serialize_json(
                value["metric_source_types"]
            )
        )
    if "metric_source" in value:
        import capo_application_signals.types.metric_source

        out["MetricSource"] = (
            capo_application_signals.types.metric_source.serialize_json(
                value["metric_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListServiceLevelObjectivesInput:
    out: ListServiceLevelObjectivesInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyAttributes") is not None:
        import capo_application_signals.types.attributes

        out["key_attributes"] = (
            capo_application_signals.types.attributes.deserialize_json(
                data["KeyAttributes"]
            )
        )
    if data.get("DependencyConfig") is not None:
        import capo_application_signals.types.dependency_config

        out["dependency_config"] = (
            capo_application_signals.types.dependency_config.deserialize_json(
                data["DependencyConfig"]
            )
        )
    if data.get("MetricSourceTypes") is not None:
        import capo_application_signals.types.metric_source_types

        out["metric_source_types"] = (
            capo_application_signals.types.metric_source_types.deserialize_json(
                data["MetricSourceTypes"]
            )
        )
    if data.get("MetricSource") is not None:
        import capo_application_signals.types.metric_source

        out["metric_source"] = (
            capo_application_signals.types.metric_source.deserialize_json(
                data["MetricSource"]
            )
        )
    return out
