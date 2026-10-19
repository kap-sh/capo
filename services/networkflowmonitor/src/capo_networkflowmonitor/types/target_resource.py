"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.aws_region
    import capo_networkflowmonitor.types.target_identifier


class TargetResource(TypedDict, closed=True):
    target_identifier: (
        "capo_networkflowmonitor.types.target_identifier.TargetIdentifier"
    )
    """<p>A target identifier is a pair of identifying information for a scope. A target identifier is made up of a targetID (currently always an account ID) and a targetType (currently always an account).</p>"""
    region: "capo_networkflowmonitor.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region for the scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetResource) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.target_identifier

    out["targetIdentifier"] = (
        capo_networkflowmonitor.types.target_identifier.serialize_json(
            value["target_identifier"]
        )
    )
    out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> TargetResource:
    out: TargetResource = {}  # type: ignore[typeddict-item]
    if data.get("targetIdentifier") is not None:
        import capo_networkflowmonitor.types.target_identifier

        out["target_identifier"] = (
            capo_networkflowmonitor.types.target_identifier.deserialize_json(
                data["targetIdentifier"]
            )
        )
    else:
        raise DeserializationError("TargetResource.target_identifier required")
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    return out
