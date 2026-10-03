"""Generated from Smithy shape ``com.amazonaws.ssm#PatchSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.patch_source_configuration
    import capo_ssm.types.patch_source_name
    import capo_ssm.types.patch_source_product_list


class PatchSource(TypedDict, closed=True):
    name: "capo_ssm.types.patch_source_name.PatchSourceName"
    """<p>The name specified to identify the patch source.</p>"""
    products: "capo_ssm.types.patch_source_product_list.PatchSourceProductList"
    """<p>The specific operating system versions a patch repository applies to, such as "Ubuntu16.04", "AmazonLinux2016.09", "RedhatEnterpriseLinux7.2" or "Suse12.7". For lists of supported product values, see <a>PatchFilter</a>.</p>"""
    configuration: "capo_ssm.types.patch_source_configuration.PatchSourceConfiguration"
    """<p>The value of the repo configuration.</p> <p> <b>Example for yum repositories</b> </p> <p> <code>[main]</code> </p> <p> <code>name=MyCustomRepository</code> </p> <p> <code>baseurl=https://my-custom-repository</code> </p> <p> <code>enabled=1</code> </p> <p>For information about other options available for your yum repository configuration, see <a href="https://man7.org/linux/man-pages/man5/dnf.conf.5.html">dnf.conf(5)</a> on the <i>man7.org</i> website.</p> <p> <b>Examples for Ubuntu Server and Debian Server</b> </p> <p> <code>deb http://security.ubuntu.com/ubuntu jammy main</code> </p> <p> <code>deb https://site.example.com/debian distribution component1 component2 component3</code> </p> <p>Repo information for Ubuntu Server repositories must be specifed in a single line. For more examples and information, see <a href="https://manpages.ubuntu.com/manpages/jammy/man5/sources.list.5.html">jammy (5) sources.list.5.gz</a> on the <i>Ubuntu Server Manuals</i> website and <a href="https://wiki.debian.org/SourcesList#sources.list_format">sources.list format</a> on the <i>Debian Wiki</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_ssm.types.patch_source_product_list

    out["Products"] = capo_ssm.types.patch_source_product_list.serialize_aws_json_1_1(
        value["products"]
    )
    out["Configuration"] = value["configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchSource:
    out: PatchSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PatchSource.name required")
    if data.get("Products") is not None:
        import capo_ssm.types.patch_source_product_list

        out["products"] = (
            capo_ssm.types.patch_source_product_list.deserialize_aws_json_1_1(
                data["Products"]
            )
        )
    else:
        raise DeserializationError("PatchSource.products required")
    if data.get("Configuration") is not None:
        out["configuration"] = data["Configuration"]
    else:
        raise DeserializationError("PatchSource.configuration required")
    return out
