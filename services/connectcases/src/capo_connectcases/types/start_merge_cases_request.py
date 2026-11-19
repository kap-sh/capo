"""Generated from Smithy shape ``com.amazonaws.connectcases#StartMergeCasesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.case_id_list
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.fields_configuration_list
    import capo_connectcases.types.related_items_configuration
    import capo_connectcases.types.user_union


class StartMergeCasesRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>The unique identifier of the primary case. The primary case remains active and receives the merged field values and related items. The cases can use different templates, and the primary case keeps its template.</p>"""
    secondary_case_ids: "capo_connectcases.types.case_id_list.CaseIdList"
    """<p>The unique identifier of the secondary case to merge into the primary case. The secondary case is closed when the merge finishes. Specify exactly one case ID.</p>"""
    fields_configuration: NotRequired[
        "capo_connectcases.types.fields_configuration_list.FieldsConfigurationList"
    ]
    """<p>The fields whose values to take from the secondary case. You can only merge custom fields and the following system fields: <code>assigned_queue</code>, <code>assigned_user</code>, <code>summary</code>, and <code>case_reason</code>. If you select any other system field, the request fails with a <code>ValidationException</code>.</p> <p>For each field that can be merged, the merge works as follows:</p> <ul> <li> <p>If you select the field, the primary case gets the secondary case's value. If the secondary case's value is empty, the primary case's value is cleared.</p> </li> <li> <p>If you don't select the field and the primary case has a value for it, the primary case keeps its value.</p> </li> <li> <p>If you don't select the field and the primary case doesn't have the field, or its value is empty, the primary case gets the secondary case's value. This applies even when the field isn't on the primary case's template.</p> </li> </ul> <p>Field values are read from both cases when the merge runs, so changes that you make to the primary case after you start the merge are taken into account.</p> <p>Specify at most one entry, and set its <code>sourceCaseId</code> to the secondary case ID.</p>"""
    related_items_configuration: NotRequired[
        "capo_connectcases.types.related_items_configuration.RelatedItemsConfiguration"
    ]
    """<p>The types of related items to move from the secondary case to the primary case. Related items of a type that you don't select, or set to <code>false</code>, stay on the closed secondary case. If you omit this parameter, no related items are moved.</p> <p>File, SLA, and work plan related items are never moved. They stay on the secondary case.</p>"""
    performed_by: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    """<p>The user who performed the merge. If you provide <code>userArn</code>, you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of that user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMergeCasesRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.case_id_list

    out["secondaryCaseIds"] = capo_connectcases.types.case_id_list.serialize_json(
        value["secondary_case_ids"]
    )
    if "fields_configuration" in value:
        import capo_connectcases.types.fields_configuration_list

        out["fieldsConfiguration"] = (
            capo_connectcases.types.fields_configuration_list.serialize_json(
                value["fields_configuration"]
            )
        )
    if "related_items_configuration" in value:
        import capo_connectcases.types.related_items_configuration

        out["relatedItemsConfiguration"] = (
            capo_connectcases.types.related_items_configuration.serialize_json(
                value["related_items_configuration"]
            )
        )
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performedBy"] = capo_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    return out


def deserialize_json(data: dict) -> StartMergeCasesRequest:
    out: StartMergeCasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("secondaryCaseIds") is not None:
        import capo_connectcases.types.case_id_list

        out["secondary_case_ids"] = (
            capo_connectcases.types.case_id_list.deserialize_json(
                data["secondaryCaseIds"]
            )
        )
    else:
        out["secondary_case_ids"] = []
    if data.get("fieldsConfiguration") is not None:
        import capo_connectcases.types.fields_configuration_list

        out["fields_configuration"] = (
            capo_connectcases.types.fields_configuration_list.deserialize_json(
                data["fieldsConfiguration"]
            )
        )
    if data.get("relatedItemsConfiguration") is not None:
        import capo_connectcases.types.related_items_configuration

        out["related_items_configuration"] = (
            capo_connectcases.types.related_items_configuration.deserialize_json(
                data["relatedItemsConfiguration"]
            )
        )
    if data.get("performedBy") is not None:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    return out


def redact_sensitive(value: StartMergeCasesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "performed_by" in value:
        import capo_connectcases.types.user_union

        out["performed_by"] = capo_connectcases.types.user_union.redact_sensitive(
            value["performed_by"]
        )
    return out
