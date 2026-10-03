"""Generated from Smithy shape ``com.amazonaws.iam#GenerateServiceLastAccessedDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.job_id_type


class GenerateServiceLastAccessedDetailsResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_iam.types.job_id_type.jobIDType"]
    """<p>The <code>JobId</code> that you can use in the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetails.html">GetServiceLastAccessedDetails</a> or <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLastAccessedDetailsWithEntities.html">GetServiceLastAccessedDetailsWithEntities</a> operations. The <code>JobId</code> returned by <code>GenerateServiceLastAccessedDetail</code> must be used by the same role within a session, or by the same user when used to call <code>GetServiceLastAccessedDetail</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GenerateServiceLastAccessedDetailsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "job_id" in value:
        pairs.append((f"{key_prefix}JobId", str(value["job_id"])))


def deserialize_query(el: Element) -> GenerateServiceLastAccessedDetailsResponse:
    out: GenerateServiceLastAccessedDetailsResponse = {}  # type: ignore[typeddict-item]
    child_job_id = el.find("JobId")
    if child_job_id is not None:
        out["job_id"] = str(child_job_id.text or "")
    return out
