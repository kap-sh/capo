"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseEventIncludedData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.auto_include_fields
    import capo_connectcases.types.field_identifier_list


class CaseEventIncludedData(TypedDict, closed=True):
    fields: "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
    """<p>List of field identifiers to include in case event data.</p>"""
    auto_include_fields: NotRequired[
        "capo_connectcases.types.auto_include_fields.AutoIncludeFields"
    ]
    """<p>Automatically include a category of fields in case event data, combined as a union with any fields specified in <code>fields</code>. Valid values are <code>All</code> (include all fields on the case), <code>System</code> (include all system fields), and <code>Custom</code> (include all custom fields). When this attribute is set, new fields added to the domain are picked up automatically without another call to PutCaseEventConfiguration. For the full behavior matrix and IAM requirements, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-event-streams.html">Case event streams in Connect Customer Cases</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseEventIncludedData) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_identifier_list

    out["fields"] = capo_connectcases.types.field_identifier_list.serialize_json(
        value["fields"]
    )
    if "auto_include_fields" in value:
        out["autoIncludeFields"] = value["auto_include_fields"]
    return out


def deserialize_json(data: dict) -> CaseEventIncludedData:
    out: CaseEventIncludedData = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_connectcases.types.field_identifier_list

        out["fields"] = capo_connectcases.types.field_identifier_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    if data.get("autoIncludeFields") is not None:
        out["auto_include_fields"] = data["autoIncludeFields"]
    return out
