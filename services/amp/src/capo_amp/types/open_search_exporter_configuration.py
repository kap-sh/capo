"""Generated from Smithy shape ``com.amazonaws.amp#OpenSearchExporterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.open_search_domain_arn


class OpenSearchExporterConfiguration(TypedDict, closed=True):
    domain_arn: "capo_amp.types.open_search_domain_arn.OpenSearchDomainArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon OpenSearch Service domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenSearchExporterConfiguration) -> dict:
    out: dict = {}
    out["domainArn"] = value["domain_arn"]
    return out


def deserialize_json(data: dict) -> OpenSearchExporterConfiguration:
    out: OpenSearchExporterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        out["domain_arn"] = ""
    return out
