"""Generated from Smithy shape ``com.amazonaws.ivs#DeleteFailoverSlateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.failover_slate_configuration_arn


class DeleteFailoverSlateConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.failover_slate_configuration_arn.FailoverSlateConfigurationArn"
    """<p>ARN of the failover slate configuration to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFailoverSlateConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteFailoverSlateConfigurationRequest:
    out: DeleteFailoverSlateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
