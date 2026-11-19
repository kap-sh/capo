"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CrlDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rolesanywhere.types.alias_name
    import capo_rolesanywhere.types.crl_alias_arn
    import capo_rolesanywhere.types.crl_resource_arn
    import capo_rolesanywhere.types.trust_anchor_resource_arn
    import capo_rolesanywhere.types.uuid


class CrlDetail(TypedDict, closed=True):
    crl_id: NotRequired["capo_rolesanywhere.types.uuid.Uuid"]
    """<p>The unique identifier of the certificate revocation list (CRL).</p>"""
    crl_arn: NotRequired["capo_rolesanywhere.types.crl_resource_arn.CrlResourceArn"]
    """<p>The ARN of the certificate revocation list (CRL).</p>"""
    name: NotRequired["str"]
    """<p>The name of the certificate revocation list (CRL).</p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the certificate revocation list (CRL) is enabled.</p>"""
    crl_data: NotRequired["bytes"]
    """<p>The state of the certificate revocation list (CRL) after a read or write operation.</p>"""
    trust_anchor_arn: NotRequired[
        "capo_rolesanywhere.types.trust_anchor_resource_arn.TrustAnchorResourceArn"
    ]
    """<p>The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the certificate revocation list (CRL) was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the certificate revocation list (CRL) was last updated. </p>"""
    alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias of the certificate revocation list (CRL). Present only if the CRL has an alias.</p>"""
    alias_arn: NotRequired["capo_rolesanywhere.types.crl_alias_arn.CrlAliasArn"]
    """<p>The alias ARN of the certificate revocation list (CRL), in the form <code>arn:<i>partition</i>:rolesanywhere:<i>region</i>:<i>account</i>:alias/crl/<i>alias-name</i> </code>. Present only if the CRL has an alias.</p> <p>You can use the alias ARN in place of the resource ID or ARN in the request parameters whose descriptions say that they accept an alias ARN. Don't use the alias ARN in Identity and Access Management (IAM) policies. A policy statement that names an alias ARN doesn't apply to the resource that holds the alias. Write policies with the ARN that contains the resource ID instead.</p>"""
    previous_alias_name: NotRequired["capo_rolesanywhere.types.alias_name.AliasName"]
    """<p>The alias that the resource had before the update request. IAM Roles Anywhere returns this value only in the response to an update request that changed or removed an existing alias. It isn't returned when the alias was unchanged, when the resource had no alias before the request, or by other operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrlDetail) -> dict:
    out: dict = {}
    if "crl_id" in value:
        out["crlId"] = value["crl_id"]
    if "crl_arn" in value:
        out["crlArn"] = value["crl_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "crl_data" in value:
        import capo_rolesanywhere.types._prelude.blob

        out["crlData"] = capo_rolesanywhere.types._prelude.blob.serialize_json(
            value["crl_data"]
        )
    if "trust_anchor_arn" in value:
        out["trustAnchorArn"] = value["trust_anchor_arn"]
    if "created_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["createdAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_rolesanywhere._protocol.serialize

        out["updatedAt"] = capo_rolesanywhere._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "alias_name" in value:
        out["aliasName"] = value["alias_name"]
    if "alias_arn" in value:
        out["aliasArn"] = value["alias_arn"]
    if "previous_alias_name" in value:
        out["previousAliasName"] = value["previous_alias_name"]
    return out


def deserialize_json(data: dict) -> CrlDetail:
    out: CrlDetail = {}  # type: ignore[typeddict-item]
    if data.get("crlId") is not None:
        out["crl_id"] = data["crlId"]
    if data.get("crlArn") is not None:
        out["crl_arn"] = data["crlArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    if data.get("crlData") is not None:
        import capo_rolesanywhere.types._prelude.blob

        out["crl_data"] = capo_rolesanywhere.types._prelude.blob.deserialize_json(
            data["crlData"]
        )
    if data.get("trustAnchorArn") is not None:
        out["trust_anchor_arn"] = data["trustAnchorArn"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("aliasName") is not None:
        out["alias_name"] = data["aliasName"]
    if data.get("aliasArn") is not None:
        out["alias_arn"] = data["aliasArn"]
    if data.get("previousAliasName") is not None:
        out["previous_alias_name"] = data["previousAliasName"]
    return out
