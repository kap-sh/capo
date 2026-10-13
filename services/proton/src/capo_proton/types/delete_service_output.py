"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.service


class DeleteServiceOutput(TypedDict, closed=True):
    service: NotRequired["capo_proton.types.service.Service"]
    """<p>The detailed data of the service being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceOutput) -> dict:
    out: dict = {}
    if "service" in value:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.serialize_aws_json_1_0(
            value["service"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceOutput:
    out: DeleteServiceOutput = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.deserialize_aws_json_1_0(
            data["service"]
        )
    return out


def redact_sensitive(value: DeleteServiceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.redact_sensitive(value["service"])
    return out
