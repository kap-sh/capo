"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_name


class CreateDomainRequest(TypedDict, closed=True):
    name: "capo_connectcases.types.domain_name.DomainName"
    """<p>The name for your Cases domain. It must be unique for your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateDomainRequest:
    out: CreateDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
