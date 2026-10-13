"""Generated from Smithy shape ``com.amazonaws.proton#CreateServiceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.service


class CreateServiceOutput(TypedDict, closed=True):
    service: "capo_proton.types.service.Service"
    """<p>The service detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceOutput) -> dict:
    out: dict = {}
    import capo_proton.types.service

    out["service"] = capo_proton.types.service.serialize_aws_json_1_0(value["service"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceOutput:
    out: CreateServiceOutput = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.deserialize_aws_json_1_0(
            data["service"]
        )
    else:
        raise DeserializationError("CreateServiceOutput.service required")
    return out


def redact_sensitive(value: CreateServiceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_proton.types.service

        out["service"] = capo_proton.types.service.redact_sensitive(value["service"])
    return out
