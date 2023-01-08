
        lblName = Label(Dataframe, text="flight id", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=7, column=5)
        comGender = ttk.Combobox(Dataframe, font=(
            "arial", 12, "bold"), width=33, textvariable=self.flight_ID)
        comGender["values"] = ("M", "F")
        comGender.grid(row=7, column=6, sticky=W)