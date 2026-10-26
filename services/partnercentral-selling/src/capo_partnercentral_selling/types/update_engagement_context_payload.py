"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UpdateEngagementContextPayload``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError, SerializationError
from capo_partnercentral_selling.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.customer_projects_context
    import capo_partnercentral_selling.types.prospecting_result
    import capo_partnercentral_selling.types.update_lead_context


class _UpdateEngagementContextPayload_Lead(TypedDict, closed=True):
    Lead: "capo_partnercentral_selling.types.update_lead_context.UpdateLeadContext"


class _UpdateEngagementContextPayload_CustomerProject(TypedDict, closed=True):
    CustomerProject: "capo_partnercentral_selling.types.customer_projects_context.CustomerProjectsContext"


class _UpdateEngagementContextPayload_ProspectingResult(TypedDict, closed=True):
    ProspectingResult: (
        "capo_partnercentral_selling.types.prospecting_result.ProspectingResult"
    )


UpdateEngagementContextPayload: TypeAlias = (
    _UpdateEngagementContextPayload_Lead
    | _UpdateEngagementContextPayload_CustomerProject
    | _UpdateEngagementContextPayload_ProspectingResult
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEngagementContextPayload) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpdateEngagementContextPayload: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Lead" in value:
        import capo_partnercentral_selling.types.update_lead_context

        return {
            "Lead": capo_partnercentral_selling.types.update_lead_context.serialize_aws_json_1_0(
                value["Lead"]
            )
        }
    elif "CustomerProject" in value:
        import capo_partnercentral_selling.types.customer_projects_context

        return {
            "CustomerProject": capo_partnercentral_selling.types.customer_projects_context.serialize_aws_json_1_0(
                value["CustomerProject"]
            )
        }
    elif "ProspectingResult" in value:
        import capo_partnercentral_selling.types.prospecting_result

        return {
            "ProspectingResult": capo_partnercentral_selling.types.prospecting_result.serialize_aws_json_1_0(
                value["ProspectingResult"]
            )
        }
    else:
        raise SerializationError("UpdateEngagementContextPayload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> UpdateEngagementContextPayload:
    if data.get("Lead") is not None:
        import capo_partnercentral_selling.types.update_lead_context

        return {
            "Lead": capo_partnercentral_selling.types.update_lead_context.deserialize_aws_json_1_0(
                data["Lead"]
            )
        }
    elif data.get("CustomerProject") is not None:
        import capo_partnercentral_selling.types.customer_projects_context

        return {
            "CustomerProject": capo_partnercentral_selling.types.customer_projects_context.deserialize_aws_json_1_0(
                data["CustomerProject"]
            )
        }
    elif data.get("ProspectingResult") is not None:
        import capo_partnercentral_selling.types.prospecting_result

        return {
            "ProspectingResult": capo_partnercentral_selling.types.prospecting_result.deserialize_aws_json_1_0(
                data["ProspectingResult"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "UpdateEngagementContextPayload: no recognized variant key"
        )


def redact_sensitive(value: UpdateEngagementContextPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Lead" in value:
        import capo_partnercentral_selling.types.update_lead_context

        out["Lead"] = (
            capo_partnercentral_selling.types.update_lead_context.redact_sensitive(
                value["Lead"]
            )
        )
    if "CustomerProject" in value:
        import capo_partnercentral_selling.types.customer_projects_context

        out["CustomerProject"] = (
            capo_partnercentral_selling.types.customer_projects_context.redact_sensitive(
                value["CustomerProject"]
            )
        )
    if "ProspectingResult" in value:
        import capo_partnercentral_selling.types.prospecting_result

        out["ProspectingResult"] = (
            capo_partnercentral_selling.types.prospecting_result.redact_sensitive(
                value["ProspectingResult"]
            )
        )
    return out
