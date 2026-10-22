"""Generated from Smithy shape ``com.amazonaws.elasticache#SecretManagerAuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class SecretManagerAuthConfig(TypedDict, closed=True):
    secret_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ARN of the secret in AWS Secrets Manager that contains the credentials for authenticating with the source.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SecretManagerAuthConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "secret_arn" in value:
        pairs.append((f"{key_prefix}SecretArn", str(value["secret_arn"])))


def deserialize_query(el: Element) -> SecretManagerAuthConfig:
    out: SecretManagerAuthConfig = {}  # type: ignore[typeddict-item]
    child_secret_arn = el.find("SecretArn")
    if child_secret_arn is not None:
        out["secret_arn"] = str(child_secret_arn.text or "")
    return out
