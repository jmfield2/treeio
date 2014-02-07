require "fileinto";

if header :contains ["Subject"] ["Inquiry Message", "hotel reservation"] {
	fileinto "Inquiries";
}
