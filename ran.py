if __name__ == "__main__":
	try:
		__import__("cek_enc").licensi()
	except Exception as e:
		exit(str(e))
