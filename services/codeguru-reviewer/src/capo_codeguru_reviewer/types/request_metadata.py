"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RequestMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.event_info
    import capo_codeguru_reviewer.types.request_id
    import capo_codeguru_reviewer.types.requester
    import capo_codeguru_reviewer.types.vendor_name


class RequestMetadata(TypedDict, closed=True):
    request_id: NotRequired["capo_codeguru_reviewer.types.request_id.RequestId"]
    """<p>The ID of the request. This is required for a pull request code review.</p>"""
    requester: NotRequired["capo_codeguru_reviewer.types.requester.Requester"]
    """<p>An identifier, such as a name or account ID, that is associated with the requester. The <code>Requester</code> is used to capture the <code>author/actor</code> name of the event request.</p>"""
    event_info: NotRequired["capo_codeguru_reviewer.types.event_info.EventInfo"]
    """<p>Information about the event associated with a code review.</p>"""
    vendor_name: NotRequired["capo_codeguru_reviewer.types.vendor_name.VendorName"]
    """<p>The name of the repository vendor used to upload code to an S3 bucket for a CI/CD code review. For example, if code and artifacts are uploaded to an S3 bucket for a CI/CD code review by GitHub scripts from a GitHub repository, then the repository association's <code>ProviderType</code> is <code>S3Bucket</code> and the CI/CD repository vendor name is GitHub. For more information, see the definition for <code>ProviderType</code> in <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestMetadata) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "requester" in value:
        out["Requester"] = value["requester"]
    if "event_info" in value:
        import capo_codeguru_reviewer.types.event_info

        out["EventInfo"] = capo_codeguru_reviewer.types.event_info.serialize_json(
            value["event_info"]
        )
    if "vendor_name" in value:
        import capo_codeguru_reviewer.types.vendor_name

        out["VendorName"] = capo_codeguru_reviewer.types.vendor_name.serialize_json(
            value["vendor_name"]
        )
    return out


def deserialize_json(data: dict) -> RequestMetadata:
    out: RequestMetadata = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("Requester") is not None:
        out["requester"] = data["Requester"]
    if data.get("EventInfo") is not None:
        import capo_codeguru_reviewer.types.event_info

        out["event_info"] = capo_codeguru_reviewer.types.event_info.deserialize_json(
            data["EventInfo"]
        )
    if data.get("VendorName") is not None:
        import capo_codeguru_reviewer.types.vendor_name

        out["vendor_name"] = capo_codeguru_reviewer.types.vendor_name.deserialize_json(
            data["VendorName"]
        )
    return out
