"""Generated from Smithy shape ``com.amazonaws.voiceid#UpdateDomainResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain


class UpdateDomainResponse(TypedDict, closed=True):
    domain: NotRequired["capo_voice_id.types.domain.Domain"]
    """<p>Details about the updated domain</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDomainResponse) -> dict:
    out: dict = {}
    if "domain" in value:
        import capo_voice_id.types.domain

        out["Domain"] = capo_voice_id.types.domain.serialize_aws_json_1_0(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDomainResponse:
    out: UpdateDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        import capo_voice_id.types.domain

        out["domain"] = capo_voice_id.types.domain.deserialize_aws_json_1_0(
            data["Domain"]
        )
    return out


def redact_sensitive(value: UpdateDomainResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "domain" in value:
        import capo_voice_id.types.domain

        out["domain"] = capo_voice_id.types.domain.redact_sensitive(value["domain"])
    return out
