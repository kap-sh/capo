"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceRegistryLogin``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.sensitive_string
    import capo_lightsail.types.string


class ContainerServiceRegistryLogin(TypedDict, closed=True):
    username: NotRequired["capo_lightsail.types.string.string"]
    """<p>The container service registry username to use to push container images to the container image registry of a Lightsail account.</p>"""
    password: NotRequired["capo_lightsail.types.sensitive_string.SensitiveString"]
    """<p>The container service registry password to use to push container images to the container image registry of a Lightsail account</p>"""
    expires_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp of when the container image registry sign-in credentials expire.</p> <p>The log in credentials expire 12 hours after they are created, at which point you will need to create a new set of log in credentials using the <code>CreateContainerServiceRegistryLogin</code> action.</p>"""
    registry: NotRequired["capo_lightsail.types.string.string"]
    """<p>The address to use to push container images to the container image registry of a Lightsail account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceRegistryLogin) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "password" in value:
        out["password"] = value["password"]
    if "expires_at" in value:
        import capo_lightsail.types.iso_date

        out["expiresAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["expires_at"]
        )
    if "registry" in value:
        out["registry"] = value["registry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceRegistryLogin:
    out: ContainerServiceRegistryLogin = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("password") is not None:
        out["password"] = data["password"]
    if data.get("expiresAt") is not None:
        import capo_lightsail.types.iso_date

        out["expires_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["expiresAt"]
        )
    if data.get("registry") is not None:
        out["registry"] = data["registry"]
    return out


def redact_sensitive(value: ContainerServiceRegistryLogin) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
