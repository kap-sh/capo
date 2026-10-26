"""Generated from Smithy shape ``com.amazonaws.datazone#CreateAccountPoolOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.account_pool_id
    import capo_datazone.types.account_pool_name
    import capo_datazone.types.account_source
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.resolution_strategy
    import capo_datazone.types.updated_by


class CreateAccountPoolOutput(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the domain where the account pool is created.</p>"""
    name: NotRequired["capo_datazone.types.account_pool_name.AccountPoolName"]
    """<p>The name of the account pool.</p>"""
    id: NotRequired["capo_datazone.types.account_pool_id.AccountPoolId"]
    """<p>The ID of the account pool.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the account pool.</p>"""
    resolution_strategy: NotRequired[
        "capo_datazone.types.resolution_strategy.ResolutionStrategy"
    ]
    """<p>The mechanism used to resolve the account selection from the account pool.</p>"""
    account_source: "capo_datazone.types.account_source.AccountSource"
    """<p>The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom Amazon Web Services Lambda handler. </p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The user who created the account pool.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the account pool was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the account pool was last updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who last updated the account pool.</p>"""
    domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain where the account pool is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountPoolOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "resolution_strategy" in value:
        import capo_datazone.types.resolution_strategy

        out["resolutionStrategy"] = (
            capo_datazone.types.resolution_strategy.serialize_json(
                value["resolution_strategy"]
            )
        )
    import capo_datazone.types.account_source

    out["accountSource"] = capo_datazone.types.account_source.serialize_json(
        value["account_source"]
    )
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_datazone._protocol.serialize

        out["lastUpdatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["last_updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    return out


def deserialize_json(data: dict) -> CreateAccountPoolOutput:
    out: CreateAccountPoolOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resolutionStrategy") is not None:
        import capo_datazone.types.resolution_strategy

        out["resolution_strategy"] = (
            capo_datazone.types.resolution_strategy.deserialize_json(
                data["resolutionStrategy"]
            )
        )
    if data.get("accountSource") is not None:
        import capo_datazone.types.account_source

        out["account_source"] = capo_datazone.types.account_source.deserialize_json(
            data["accountSource"]
        )
    else:
        out["account_source"] = {"$unknown": {"name": ""}}
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("lastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["lastUpdatedAt"].replace("Z", "+00:00")
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    return out


def redact_sensitive(value: CreateAccountPoolOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "account_source" in value:
        import capo_datazone.types.account_source

        out["account_source"] = capo_datazone.types.account_source.redact_sensitive(
            value["account_source"]
        )
    return out
