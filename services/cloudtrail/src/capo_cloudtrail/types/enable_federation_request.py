"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EnableFederationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.federation_role_arn


class EnableFederationRequest(TypedDict, closed=True):
    event_data_store: "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p>The ARN (or ID suffix of the ARN) of the event data store for which you want to enable Lake query federation.</p>"""
    federation_role_arn: "capo_cloudtrail.types.federation_role_arn.FederationRoleArn"
    """<p> The ARN of the federation role to use for the event data store. Amazon Web Services services like Lake Formation use this federation role to access data for the federated event data store. The federation role must exist in your account and provide the <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html#query-federation-permissions-role">required minimum permissions</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableFederationRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    out["FederationRoleArn"] = value["federation_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableFederationRequest:
    out: EnableFederationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStore") is not None:
        out["event_data_store"] = data["EventDataStore"]
    else:
        raise DeserializationError("EnableFederationRequest.event_data_store required")
    if data.get("FederationRoleArn") is not None:
        out["federation_role_arn"] = data["FederationRoleArn"]
    else:
        raise DeserializationError(
            "EnableFederationRequest.federation_role_arn required"
        )
    return out
