"""Generated from Smithy shape ``com.amazonaws.transfer#ListCertificatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listed_certificates
    import capo_transfer.types.next_token


class ListCertificatesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>Returns the next token, which you can use to list the next certificate.</p>"""
    certificates: "capo_transfer.types.listed_certificates.ListedCertificates"
    """<p>Returns an array of the certificates that are specified in the <code>ListCertificates</code> call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_transfer.types.listed_certificates

    out["Certificates"] = (
        capo_transfer.types.listed_certificates.serialize_aws_json_1_1(
            value["certificates"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificatesResponse:
    out: ListCertificatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Certificates") is not None:
        import capo_transfer.types.listed_certificates

        out["certificates"] = (
            capo_transfer.types.listed_certificates.deserialize_aws_json_1_1(
                data["Certificates"]
            )
        )
    else:
        out["certificates"] = []
    return out
