"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OverallTestResults``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.overall_test_result_item_list


class OverallTestResults(TypedDict, closed=True):
    items: "capo_lex_models_v2.types.overall_test_result_item_list.OverallTestResultItemList"
    """<p>A list of the overall test results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverallTestResults) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.overall_test_result_item_list

    out["items"] = (
        capo_lex_models_v2.types.overall_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> OverallTestResults:
    out: OverallTestResults = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_lex_models_v2.types.overall_test_result_item_list

        out["items"] = (
            capo_lex_models_v2.types.overall_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    return out
