"""Generated from Smithy shape ``com.amazonaws.drs#StartSourceNetworkRecoveryRequestNetworkEntry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_drs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_drs.types.cfn_stack_name
    import capo_drs.types.source_network_id


class StartSourceNetworkRecoveryRequestNetworkEntry(TypedDict, closed=True):
    source_network_id: "capo_drs.types.source_network_id.SourceNetworkID"
    """<p>The ID of the Source Network you want to recover.</p>"""
    cfn_stack_name: NotRequired["capo_drs.types.cfn_stack_name.CfnStackName"]
    """<p>CloudFormation stack name to be used for recovering the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSourceNetworkRecoveryRequestNetworkEntry) -> dict:
    out: dict = {}
    out["sourceNetworkID"] = value["source_network_id"]
    if "cfn_stack_name" in value:
        out["cfnStackName"] = value["cfn_stack_name"]
    return out


def deserialize_json(data: dict) -> StartSourceNetworkRecoveryRequestNetworkEntry:
    out: StartSourceNetworkRecoveryRequestNetworkEntry = {}  # type: ignore[typeddict-item]
    if data.get("sourceNetworkID") is not None:
        out["source_network_id"] = data["sourceNetworkID"]
    else:
        raise DeserializationError(
            "StartSourceNetworkRecoveryRequestNetworkEntry.source_network_id required"
        )
    if data.get("cfnStackName") is not None:
        out["cfn_stack_name"] = data["cfnStackName"]
    return out


def redact_sensitive(
    value: StartSourceNetworkRecoveryRequestNetworkEntry,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cfn_stack_name" in value:
        out["cfn_stack_name"] = "*** Sensitive Data Redacted ***"
    return out
