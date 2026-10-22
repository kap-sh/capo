"""Generated from Smithy shape ``com.amazonaws.elasticache#SourceAuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.secret_manager_auth_config


class SourceAuthenticationConfiguration(TypedDict, closed=True):
    secret_manager_config: NotRequired[
        "capo_elasticache.types.secret_manager_auth_config.SecretManagerAuthConfig"
    ]
    """<p>The Secrets Manager configuration used for authenticating with the source during migration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceAuthenticationConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "secret_manager_config" in value:
        import capo_elasticache.types.secret_manager_auth_config

        capo_elasticache.types.secret_manager_auth_config.serialize_query(
            value["secret_manager_config"], pairs, f"{key_prefix}SecretManagerConfig"
        )


def deserialize_query(el: Element) -> SourceAuthenticationConfiguration:
    out: SourceAuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    child_secret_manager_config = el.find("SecretManagerConfig")
    if child_secret_manager_config is not None:
        import capo_elasticache.types.secret_manager_auth_config

        out["secret_manager_config"] = (
            capo_elasticache.types.secret_manager_auth_config.deserialize_query(
                child_secret_manager_config
            )
        )
    return out
