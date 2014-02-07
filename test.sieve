require "fileinto";
if header :contains ["From", "To"] ["root2"] {
	discard;
}
