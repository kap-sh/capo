"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorChecksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.string


class DescribeTrustedAdvisorChecksRequest(TypedDict, closed=True):
    language: "capo_support.types.string.String"
    """<p>The ISO 639-1 code for the language that you want your checks to appear in.</p> <p>The Amazon Web Services Support API currently supports the following languages for Trusted Advisor:</p> <ul> <li> <p>Chinese, Simplified - <code>zh</code> </p> </li> <li> <p>Chinese, Traditional - <code>zh_TW</code> </p> </li> <li> <p>English - <code>en</code> </p> </li> <li> <p>French - <code>fr</code> </p> </li> <li> <p>German - <code>de</code> </p> </li> <li> <p>Indonesian - <code>id</code> </p> </li> <li> <p>Italian - <code>it</code> </p> </li> <li> <p>Japanese - <code>ja</code> </p> </li> <li> <p>Korean - <code>ko</code> </p> </li> <li> <p>Portuguese, Brazilian - <code>pt_BR</code> </p> </li> <li> <p>Spanish - <code>es</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedAdvisorChecksRequest) -> dict:
    out: dict = {}
    out["language"] = value["language"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustedAdvisorChecksRequest:
    out: DescribeTrustedAdvisorChecksRequest = {}  # type: ignore[typeddict-item]
    if data.get("language") is not None:
        out["language"] = data["language"]
    else:
        out["language"] = ""
    return out
