"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_status_list


class DescribeDomainsResponse(TypedDict, closed=True):
    domain_status_list: "capo_cloudsearch.types.domain_status_list.DomainStatusList"


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDomainsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_cloudsearch.types.domain_status_list

    capo_cloudsearch.types.domain_status_list.serialize_query(
        value["domain_status_list"], pairs, f"{key_prefix}DomainStatusList"
    )


def deserialize_query(el: Element) -> DescribeDomainsResponse:
    out: DescribeDomainsResponse = {}  # type: ignore[typeddict-item]
    child_domain_status_list = el.find("DomainStatusList")
    if child_domain_status_list is not None:
        import capo_cloudsearch.types.domain_status_list

        out["domain_status_list"] = (
            capo_cloudsearch.types.domain_status_list.deserialize_query(
                child_domain_status_list
            )
        )
    else:
        out["domain_status_list"] = []
    return out
