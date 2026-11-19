"""Generated from Smithy shape ``com.amazonaws.fms#EntryViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.entries_with_conflicts
    import capo_fms.types.entry_description
    import capo_fms.types.entry_violation_reasons
    import capo_fms.types.length_bounded_string


class EntryViolation(TypedDict, closed=True):
    expected_entry: NotRequired["capo_fms.types.entry_description.EntryDescription"]
    """<p>The Firewall Manager-managed network ACL entry that is involved in the entry violation. </p>"""
    expected_evaluation_order: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The evaluation location within the ordered list of entries where the <code>ExpectedEntry</code> should be, according to the network ACL policy specifications. </p>"""
    actual_evaluation_order: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The evaluation location within the ordered list of entries where the <code>ExpectedEntry</code> is currently located. </p>"""
    entry_at_expected_evaluation_order: NotRequired[
        "capo_fms.types.entry_description.EntryDescription"
    ]
    """<p>The entry that's currently in the <code>ExpectedEvaluationOrder</code> location, in place of the expected entry. </p>"""
    entries_with_conflicts: NotRequired[
        "capo_fms.types.entries_with_conflicts.EntriesWithConflicts"
    ]
    """<p>The list of entries that are in conflict with <code>ExpectedEntry</code>. </p>"""
    entry_violation_reasons: NotRequired[
        "capo_fms.types.entry_violation_reasons.EntryViolationReasons"
    ]
    """<p>Descriptions of the violations that Firewall Manager found for these entries. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntryViolation) -> dict:
    out: dict = {}
    if "expected_entry" in value:
        import capo_fms.types.entry_description

        out["ExpectedEntry"] = capo_fms.types.entry_description.serialize_aws_json_1_1(
            value["expected_entry"]
        )
    if "expected_evaluation_order" in value:
        out["ExpectedEvaluationOrder"] = value["expected_evaluation_order"]
    if "actual_evaluation_order" in value:
        out["ActualEvaluationOrder"] = value["actual_evaluation_order"]
    if "entry_at_expected_evaluation_order" in value:
        import capo_fms.types.entry_description

        out["EntryAtExpectedEvaluationOrder"] = (
            capo_fms.types.entry_description.serialize_aws_json_1_1(
                value["entry_at_expected_evaluation_order"]
            )
        )
    if "entries_with_conflicts" in value:
        import capo_fms.types.entries_with_conflicts

        out["EntriesWithConflicts"] = (
            capo_fms.types.entries_with_conflicts.serialize_aws_json_1_1(
                value["entries_with_conflicts"]
            )
        )
    if "entry_violation_reasons" in value:
        import capo_fms.types.entry_violation_reasons

        out["EntryViolationReasons"] = (
            capo_fms.types.entry_violation_reasons.serialize_aws_json_1_1(
                value["entry_violation_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntryViolation:
    out: EntryViolation = {}  # type: ignore[typeddict-item]
    if data.get("ExpectedEntry") is not None:
        import capo_fms.types.entry_description

        out["expected_entry"] = (
            capo_fms.types.entry_description.deserialize_aws_json_1_1(
                data["ExpectedEntry"]
            )
        )
    if data.get("ExpectedEvaluationOrder") is not None:
        out["expected_evaluation_order"] = data["ExpectedEvaluationOrder"]
    if data.get("ActualEvaluationOrder") is not None:
        out["actual_evaluation_order"] = data["ActualEvaluationOrder"]
    if data.get("EntryAtExpectedEvaluationOrder") is not None:
        import capo_fms.types.entry_description

        out["entry_at_expected_evaluation_order"] = (
            capo_fms.types.entry_description.deserialize_aws_json_1_1(
                data["EntryAtExpectedEvaluationOrder"]
            )
        )
    if data.get("EntriesWithConflicts") is not None:
        import capo_fms.types.entries_with_conflicts

        out["entries_with_conflicts"] = (
            capo_fms.types.entries_with_conflicts.deserialize_aws_json_1_1(
                data["EntriesWithConflicts"]
            )
        )
    if data.get("EntryViolationReasons") is not None:
        import capo_fms.types.entry_violation_reasons

        out["entry_violation_reasons"] = (
            capo_fms.types.entry_violation_reasons.deserialize_aws_json_1_1(
                data["EntryViolationReasons"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntryViolation) -> dict:
    out: dict = {}
    if "expected_entry" in value:
        import capo_fms.types.entry_description

        out["ExpectedEntry"] = capo_fms.types.entry_description.serialize_cbor(
            value["expected_entry"]
        )
    if "expected_evaluation_order" in value:
        out["ExpectedEvaluationOrder"] = value["expected_evaluation_order"]
    if "actual_evaluation_order" in value:
        out["ActualEvaluationOrder"] = value["actual_evaluation_order"]
    if "entry_at_expected_evaluation_order" in value:
        import capo_fms.types.entry_description

        out["EntryAtExpectedEvaluationOrder"] = (
            capo_fms.types.entry_description.serialize_cbor(
                value["entry_at_expected_evaluation_order"]
            )
        )
    if "entries_with_conflicts" in value:
        import capo_fms.types.entries_with_conflicts

        out["EntriesWithConflicts"] = (
            capo_fms.types.entries_with_conflicts.serialize_cbor(
                value["entries_with_conflicts"]
            )
        )
    if "entry_violation_reasons" in value:
        import capo_fms.types.entry_violation_reasons

        out["EntryViolationReasons"] = (
            capo_fms.types.entry_violation_reasons.serialize_cbor(
                value["entry_violation_reasons"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EntryViolation:
    out: EntryViolation = {}  # type: ignore[typeddict-item]
    if data.get("ExpectedEntry") is not None:
        import capo_fms.types.entry_description

        out["expected_entry"] = capo_fms.types.entry_description.deserialize_cbor(
            data["ExpectedEntry"]
        )
    if data.get("ExpectedEvaluationOrder") is not None:
        out["expected_evaluation_order"] = data["ExpectedEvaluationOrder"]
    if data.get("ActualEvaluationOrder") is not None:
        out["actual_evaluation_order"] = data["ActualEvaluationOrder"]
    if data.get("EntryAtExpectedEvaluationOrder") is not None:
        import capo_fms.types.entry_description

        out["entry_at_expected_evaluation_order"] = (
            capo_fms.types.entry_description.deserialize_cbor(
                data["EntryAtExpectedEvaluationOrder"]
            )
        )
    if data.get("EntriesWithConflicts") is not None:
        import capo_fms.types.entries_with_conflicts

        out["entries_with_conflicts"] = (
            capo_fms.types.entries_with_conflicts.deserialize_cbor(
                data["EntriesWithConflicts"]
            )
        )
    if data.get("EntryViolationReasons") is not None:
        import capo_fms.types.entry_violation_reasons

        out["entry_violation_reasons"] = (
            capo_fms.types.entry_violation_reasons.deserialize_cbor(
                data["EntryViolationReasons"]
            )
        )
    return out
