"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.service


class GetServiceOutput(TypedDict, closed=True):
    service: NotRequired["capo_proton.types.service.Service"]
    """<p>The detailed data of the requested service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceOutput) -> dict:
    out: dict = {}
    if "service" in value:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.serialize_aws_json_1_0(
            value["service"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceOutput:
    out: GetServiceOutput = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.deserialize_aws_json_1_0(
            data["service"]
        )
    return out


def redact_sensitive(value: GetServiceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.redact_sensitive(value["service"])
    return out
