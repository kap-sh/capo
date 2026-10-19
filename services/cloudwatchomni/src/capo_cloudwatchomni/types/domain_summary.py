"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.domain_status
    import capo_cloudwatchomni.types.identity_center_instance_arn


class DomainSummary(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The unique ID of the domain."""
    domain_arn: NotRequired["capo_cloudwatchomni.types.arn.Arn"]
    """The Amazon Resource Name (ARN) of the domain."""
    name: NotRequired["str"]
    """A name that identifies the domain."""
    identity_center_instance_arn: NotRequired[
        "capo_cloudwatchomni.types.identity_center_instance_arn.IdentityCenterInstanceArn"
    ]
    """Identity Center instance ARN configured for the domain. Absent for IAM-only domains."""
    region: NotRequired["str"]
    """The Region where this domain was created."""
    created_at: "datetime.datetime"
    """The timestamp when the domain was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the domain was last updated."""
    status: "capo_cloudwatchomni.types.domain_status.DomainStatus"
    """Current status of the domain."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "domain_arn" in value:
        out["domainArn"] = value["domain_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "identity_center_instance_arn" in value:
        out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "region" in value:
        out["region"] = value["region"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    import capo_cloudwatchomni.types.domain_status

    out["status"] = capo_cloudwatchomni.types.domain_status.serialize_cbor(
        value["status"]
    )
    return out


def deserialize_cbor(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("identityCenterInstanceArn") is not None:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_cloudwatchomni.types.domain_status

        out["status"] = capo_cloudwatchomni.types.domain_status.deserialize_cbor(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cloudwatchomni.types.domain_status.DomainStatus", ""
        )
    return out
