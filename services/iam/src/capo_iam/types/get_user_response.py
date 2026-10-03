"""Generated from Smithy shape ``com.amazonaws.iam#GetUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.user


class GetUserResponse(TypedDict, closed=True):
    user: "capo_iam.types.user.User"
    """<p>A structure containing details about the IAM user.</p> <important> <p>Due to a service issue, password last used data does not include password use from May 3, 2018 22:50 PDT to May 23, 2018 14:08 PDT. This affects <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html">last sign-in</a> dates shown in the IAM console and password last used dates in the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html">IAM credential report</a>, and returned by this operation. If users signed in during the affected time, the password last used date that is returned is the date the user last signed in before May 3, 2018. For users that signed in after May 23, 2018 14:08 PDT, the returned password last used date is accurate.</p> <p>You can use password last used information to identify unused credentials for deletion. For example, you might delete users who did not sign in to Amazon Web Services in the last 90 days. In cases like this, we recommend that you adjust your evaluation window to include dates after May 23, 2018. Alternatively, if your users use access keys to access Amazon Web Services programmatically you can refer to access key last used information because it is accurate for all dates. </p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetUserResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.user

    capo_iam.types.user.serialize_query(value["user"], pairs, f"{key_prefix}User")


def deserialize_query(el: Element) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    child_user = el.find("User")
    if child_user is not None:
        import capo_iam.types.user

        out["user"] = capo_iam.types.user.deserialize_query(child_user)
    else:
        raise DeserializationError("GetUserResponse.user required")
    return out
