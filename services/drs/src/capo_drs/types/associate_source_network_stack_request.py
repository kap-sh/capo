"""Generated from Smithy shape ``com.amazonaws.drs#AssociateSourceNetworkStackRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.cfn_stack_name
    import capo_drs.types.source_network_id


class AssociateSourceNetworkStackRequest(TypedDict, closed=True):
    source_network_id: "capo_drs.types.source_network_id.SourceNetworkID"
    """<p>The Source Network ID to associate with CloudFormation template.</p>"""
    cfn_stack_name: "capo_drs.types.cfn_stack_name.CfnStackName"
    """<p>CloudFormation template to associate with a Source Network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSourceNetworkStackRequest) -> dict:
    out: dict = {}
    out["sourceNetworkID"] = value["source_network_id"]
    out["cfnStackName"] = value["cfn_stack_name"]
    return out


def deserialize_json(data: dict) -> AssociateSourceNetworkStackRequest:
    out: AssociateSourceNetworkStackRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceNetworkID") is not None:
        out["source_network_id"] = data["sourceNetworkID"]
    else:
        raise DeserializationError(
            "AssociateSourceNetworkStackRequest.source_network_id required"
        )
    if data.get("cfnStackName") is not None:
        out["cfn_stack_name"] = data["cfnStackName"]
    else:
        raise DeserializationError(
            "AssociateSourceNetworkStackRequest.cfn_stack_name required"
        )
    return out


def redact_sensitive(value: AssociateSourceNetworkStackRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cfn_stack_name" in value:
        out["cfn_stack_name"] = "*** Sensitive Data Redacted ***"
    return out
