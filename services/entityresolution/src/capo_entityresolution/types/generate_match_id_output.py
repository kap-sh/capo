"""Generated from Smithy shape ``com.amazonaws.entityresolution#GenerateMatchIdOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.failed_records_list
    import capo_entityresolution.types.match_groups_list


class GenerateMatchIdOutput(TypedDict, closed=True):
    match_groups: "capo_entityresolution.types.match_groups_list.MatchGroupsList"
    """<p> The match groups from the generated match ID.</p>"""
    failed_records: "capo_entityresolution.types.failed_records_list.FailedRecordsList"
    """<p> The records that didn't receive a generated Match ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateMatchIdOutput) -> dict:
    out: dict = {}
    import capo_entityresolution.types.match_groups_list

    out["matchGroups"] = capo_entityresolution.types.match_groups_list.serialize_json(
        value["match_groups"]
    )
    import capo_entityresolution.types.failed_records_list

    out["failedRecords"] = (
        capo_entityresolution.types.failed_records_list.serialize_json(
            value["failed_records"]
        )
    )
    return out


def deserialize_json(data: dict) -> GenerateMatchIdOutput:
    out: GenerateMatchIdOutput = {}  # type: ignore[typeddict-item]
    if data.get("matchGroups") is not None:
        import capo_entityresolution.types.match_groups_list

        out["match_groups"] = (
            capo_entityresolution.types.match_groups_list.deserialize_json(
                data["matchGroups"]
            )
        )
    else:
        out["match_groups"] = []
    if data.get("failedRecords") is not None:
        import capo_entityresolution.types.failed_records_list

        out["failed_records"] = (
            capo_entityresolution.types.failed_records_list.deserialize_json(
                data["failedRecords"]
            )
        )
    else:
        out["failed_records"] = []
    return out
