"""Generated from Smithy shape ``com.amazonaws.s3control#GetDataAccessResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.credentials
    import capo_s3_control.types.grantee
    import capo_s3_control.types.s3_prefix


class GetDataAccessResult(TypedDict, closed=True):
    credentials: NotRequired["capo_s3_control.types.credentials.Credentials"]
    """<p>The temporary credential token that S3 Access Grants vends.</p>"""
    matched_grant_target: NotRequired["capo_s3_control.types.s3_prefix.S3Prefix"]
    """<p>The S3 URI path of the data to which you are being granted temporary access credentials. </p>"""
    grantee: NotRequired["capo_s3_control.types.grantee.Grantee"]
    """<p>The user, group, or role that was granted access to the S3 location scope. For directory identities, this API also returns the grants of the IAM role used for the identity-aware request. For more information on identity-aware sessions, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.html">Granting permissions to use identity-aware console sessions</a>. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetDataAccessResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "credentials" in value:
        import capo_s3_control.types.credentials

        capo_s3_control.types.credentials.serialize_xml(
            value["credentials"], el, "Credentials"
        )
    if "matched_grant_target" in value:
        SubElement(el, "MatchedGrantTarget").text = str(value["matched_grant_target"])
    if "grantee" in value:
        import capo_s3_control.types.grantee

        capo_s3_control.types.grantee.serialize_xml(value["grantee"], el, "Grantee")


def deserialize_xml(el: Element) -> GetDataAccessResult:
    out: GetDataAccessResult = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import capo_s3_control.types.credentials

        out["credentials"] = capo_s3_control.types.credentials.deserialize_xml(
            child_credentials
        )
    child_matched_grant_target = el.find("MatchedGrantTarget")
    if child_matched_grant_target is not None:
        out["matched_grant_target"] = str(child_matched_grant_target.text or "")
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        import capo_s3_control.types.grantee

        out["grantee"] = capo_s3_control.types.grantee.deserialize_xml(child_grantee)
    return out
