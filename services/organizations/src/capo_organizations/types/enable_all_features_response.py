"""Generated from Smithy shape ``com.amazonaws.organizations#EnableAllFeaturesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshake


class EnableAllFeaturesResponse(TypedDict, closed=True):
    handshake: NotRequired["capo_organizations.types.handshake.Handshake"]
    """<p>A structure that contains details about the handshake created to support this request to enable all features in the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableAllFeaturesResponse) -> dict:
    out: dict = {}
    if "handshake" in value:
        import capo_organizations.types.handshake

        out["Handshake"] = capo_organizations.types.handshake.serialize_aws_json_1_1(
            value["handshake"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableAllFeaturesResponse:
    out: EnableAllFeaturesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Handshake") is not None:
        import capo_organizations.types.handshake

        out["handshake"] = capo_organizations.types.handshake.deserialize_aws_json_1_1(
            data["Handshake"]
        )
    return out


def redact_sensitive(value: EnableAllFeaturesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "handshake" in value:
        import capo_organizations.types.handshake

        out["handshake"] = capo_organizations.types.handshake.redact_sensitive(
            value["handshake"]
        )
    return out
