"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeIndexFieldsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.index_field_status_list


class DescribeIndexFieldsResponse(TypedDict, closed=True):
    index_fields: "capo_cloudsearch.types.index_field_status_list.IndexFieldStatusList"
    """<p>The index fields configured for the domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeIndexFieldsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_cloudsearch.types.index_field_status_list

    capo_cloudsearch.types.index_field_status_list.serialize_query(
        value["index_fields"], pairs, f"{key_prefix}IndexFields"
    )


def deserialize_query(el: Element) -> DescribeIndexFieldsResponse:
    out: DescribeIndexFieldsResponse = {}  # type: ignore[typeddict-item]
    child_index_fields = el.find("IndexFields")
    if child_index_fields is not None:
        import capo_cloudsearch.types.index_field_status_list

        out["index_fields"] = (
            capo_cloudsearch.types.index_field_status_list.deserialize_query(
                child_index_fields
            )
        )
    else:
        out["index_fields"] = []
    return out
