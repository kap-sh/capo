"""Generated from Smithy shape ``com.amazonaws.quicksight#AmazonElasticsearchParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.domain


class AmazonElasticsearchParameters(TypedDict, closed=True):
    domain: "capo_quicksight.types.domain.Domain"
    """<p>The OpenSearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonElasticsearchParameters) -> dict:
    out: dict = {}
    out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> AmazonElasticsearchParameters:
    out: AmazonElasticsearchParameters = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        out["domain"] = ""
    return out
