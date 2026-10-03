// Maps `<service>.capo-sdk.dev/<path>` to the R2 object `<service>/<path>`,
// which is all that static hosting needs on top of what R2 does by itself:
// the subdomain picks the site, and a directory URL resolves to its index.html.
// The apex `capo-sdk.dev` is the main site, kept under the `_root/` prefix.
const APEX = "capo-sdk.dev";

export default {
  async fetch(request, env) {
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method Not Allowed", { status: 405 });
    }

    const url = new URL(request.url);
    const service = url.hostname === APEX ? "_root" : url.hostname.split(".")[0];
    let key = service + decodeURIComponent(url.pathname);
    if (key.endsWith("/")) key += "index.html";

    const object = await env.DOCS.get(key, { onlyIf: request.headers });
    if (object === null) {
      // `/page` without the trailing slash: the links inside a page are
      // relative, so it has to be redirected rather than served in place.
      if (await env.DOCS.head(`${key}/index.html`)) {
        return Response.redirect(`${url.origin}${url.pathname}/${url.search}`, 301);
      }
      const notFound = await env.DOCS.get(`${service}/404.html`);
      return new Response(notFound ? notFound.body : "Not Found", {
        status: 404,
        headers: { "content-type": "text/html; charset=utf-8" },
      });
    }

    const headers = new Headers();
    object.writeHttpMetadata(headers);
    headers.set("etag", object.httpEtag);
    // No body means the `If-None-Match` precondition failed: the browser's
    // copy is still current.
    if (!("body" in object)) return new Response(null, { status: 304, headers });
    return new Response(object.body, { headers });
  },
};
