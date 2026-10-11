"""MCP server for Dynamic Landing Page Personalizer."""
import sys
import json
from client import LandingPagePersonalizer

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "personalize_landing_page",
                "description": "Generates tailored hero copy and CTA based on visitor context",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "visitor_context": {"type": "object"}
                    },
                    "required": ["visitor_context"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "personalize_landing_page":
            ctx = params.get("arguments", {}).get("visitor_context", {})
            res = LandingPagePersonalizer.personalize_view(ctx)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
