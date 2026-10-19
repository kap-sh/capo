"""Generated from Smithy shape ``com.amazonaws.swf#UndeprecateDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.domain_name


class UndeprecateDomainInput(TypedDict, closed=True):
    name: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain of the deprecated workflow type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UndeprecateDomainInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UndeprecateDomainInput:
    out: UndeprecateDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
