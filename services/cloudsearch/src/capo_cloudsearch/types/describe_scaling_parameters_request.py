"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeScalingParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name


class DescribeScalingParametersRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeScalingParametersRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))


def deserialize_query(el: Element) -> DescribeScalingParametersRequest:
    out: DescribeScalingParametersRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    return out
