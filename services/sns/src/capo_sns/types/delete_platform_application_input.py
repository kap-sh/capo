"""Generated from Smithy shape ``com.amazonaws.sns#DeletePlatformApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.string


class DeletePlatformApplicationInput(TypedDict, closed=True):
    platform_application_arn: "capo_sns.types.string.String"
    """<p> <code>PlatformApplicationArn</code> of platform application object to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeletePlatformApplicationInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}PlatformApplicationArn", str(value["platform_application_arn"]))
    )


def deserialize_query(el: Element) -> DeletePlatformApplicationInput:
    out: DeletePlatformApplicationInput = {}  # type: ignore[typeddict-item]
    child_platform_application_arn = el.find("PlatformApplicationArn")
    if child_platform_application_arn is not None:
        out["platform_application_arn"] = str(child_platform_application_arn.text or "")
    else:
        out["platform_application_arn"] = ""
    return out
