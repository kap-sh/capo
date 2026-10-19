"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#StartQualificationsAssociationTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.partner_arn
    import capo_partnercentral_account.types.partner_id
    import capo_partnercentral_account.types.qualifications_association_partner
    import capo_partnercentral_account.types.qualifications_association_task_id
    import capo_partnercentral_account.types.qualifications_association_task_status


class StartQualificationsAssociationTaskResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier echoed from the request.</p>"""
    arn: "capo_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies your partner resource.</p>"""
    id: "capo_partnercentral_account.types.partner_id.PartnerId"
    """<p>Your unique partner identifier in the AWS Partner Network.</p>"""
    task_id: "capo_partnercentral_account.types.qualifications_association_task_id.QualificationsAssociationTaskId"
    """<p>The unique identifier of the started qualifications association task, in the format <code>pqatask-[a-z2-7]{13}</code>.</p>"""
    status: "capo_partnercentral_account.types.qualifications_association_task_status.QualificationsAssociationTaskStatus"
    """<p>The current status of the qualifications association task. The initial value is <code>IN_PROGRESS</code>.</p>"""
    primary_partner: "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner"
    """<p>The resolved primary partner's profile and account identifiers, including both <code>ProfileId</code> and <code>AccountId</code>.</p>"""
    started_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the qualifications association task started, in ISO 8601 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartQualificationsAssociationTaskResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    out["TaskId"] = value["task_id"]
    import capo_partnercentral_account.types.qualifications_association_task_status

    out["Status"] = (
        capo_partnercentral_account.types.qualifications_association_task_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_partnercentral_account.types.qualifications_association_partner

    out["PrimaryPartner"] = (
        capo_partnercentral_account.types.qualifications_association_partner.serialize_aws_json_1_0(
            value["primary_partner"]
        )
    )
    import capo_partnercentral_account.types.date_time

    out["StartedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["started_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartQualificationsAssociationTaskResponse:
    out: StartQualificationsAssociationTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    if data.get("Status") is not None:
        import capo_partnercentral_account.types.qualifications_association_task_status

        out["status"] = (
            capo_partnercentral_account.types.qualifications_association_task_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_account.types.qualifications_association_task_status.QualificationsAssociationTaskStatus",
            "",
        )
    if data.get("PrimaryPartner") is not None:
        import capo_partnercentral_account.types.qualifications_association_partner

        out["primary_partner"] = (
            capo_partnercentral_account.types.qualifications_association_partner.deserialize_aws_json_1_0(
                data["PrimaryPartner"]
            )
        )
    else:
        raise DeserializationError(
            "StartQualificationsAssociationTaskResponse.primary_partner required"
        )
    if data.get("StartedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["started_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
