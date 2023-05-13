if __name__ == "__main__":
	try:
		__import__("run_enc").licensi()
	except Exception as e:
		exit(str(e))
