"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeSuggestersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.suggester_status_list


class DescribeSuggestersResponse(TypedDict, closed=True):
    suggesters: "capo_cloudsearch.types.suggester_status_list.SuggesterStatusList"
    """<p>The suggesters configured for the domain specified in the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSuggestersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_cloudsearch.types.suggester_status_list

    capo_cloudsearch.types.suggester_status_list.serialize_query(
        value["suggesters"], pairs, f"{key_prefix}Suggesters"
    )


def deserialize_query(el: Element) -> DescribeSuggestersResponse:
    out: DescribeSuggestersResponse = {}  # type: ignore[typeddict-item]
    child_suggesters = el.find("Suggesters")
    if child_suggesters is not None:
        import capo_cloudsearch.types.suggester_status_list

        out["suggesters"] = (
            capo_cloudsearch.types.suggester_status_list.deserialize_query(
                child_suggesters
            )
        )
    else:
        out["suggesters"] = []
    return out
