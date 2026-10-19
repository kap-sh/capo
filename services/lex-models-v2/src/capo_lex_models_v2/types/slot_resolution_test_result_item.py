"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotResolutionTestResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_resolution_test_result_item_counts
    import capo_lex_models_v2.types.test_result_slot_name


class SlotResolutionTestResultItem(TypedDict, closed=True):
    slot_name: "capo_lex_models_v2.types.test_result_slot_name.TestResultSlotName"
    """<p>The name of the slot.</p>"""
    result_counts: "capo_lex_models_v2.types.slot_resolution_test_result_item_counts.SlotResolutionTestResultItemCounts"
    """<p>A result for slot resolution in the results of a test execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotResolutionTestResultItem) -> dict:
    out: dict = {}
    out["slotName"] = value["slot_name"]
    import capo_lex_models_v2.types.slot_resolution_test_result_item_counts

    out["resultCounts"] = (
        capo_lex_models_v2.types.slot_resolution_test_result_item_counts.serialize_json(
            value["result_counts"]
        )
    )
    return out


def deserialize_json(data: dict) -> SlotResolutionTestResultItem:
    out: SlotResolutionTestResultItem = {}  # type: ignore[typeddict-item]
    if data.get("slotName") is not None:
        out["slot_name"] = data["slotName"]
    else:
        out["slot_name"] = ""
    if data.get("resultCounts") is not None:
        import capo_lex_models_v2.types.slot_resolution_test_result_item_counts

        out["result_counts"] = (
            capo_lex_models_v2.types.slot_resolution_test_result_item_counts.deserialize_json(
                data["resultCounts"]
            )
        )
    else:
        raise DeserializationError(
            "SlotResolutionTestResultItem.result_counts required"
        )
    return out
