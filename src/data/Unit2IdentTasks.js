const Unit2IdentTasks = {
    tileNo: "unit2Ident",
    level: 4,
    successMessage: "🕵️‍♀️ Great work! But there's no time to loose, let's stop the attacker.",
    partSuccessMessage: "🕵️‍♀️ Great work! Never mind that you missed one task.",
    failMessage: "Don't panic, in the next phase the luck is on your side.",
    rememberMessage: "Remember you can always revisit lessons.",
    responsePhase: "identification",
    phaseIntroduction: `<div class="has-text-left">This time it is critical to get all the information right. Otherwise we risk taking down the wrong systems, causing even more disruptions!</div> <br> 
    <div class="has-text-left">To establish the scope of the incident, perform the following two steps.</div>`,
    blanks: [
        {
            level: 2,
            responseActionID: "Flag 3",
            responseActionInstruction: `<span>&#62;</span><span>&#62;</span> Identify the other target of the attack.`,
            flagInstruction: "Submit this host's IP address:",
            flagVariants: ["10.0.0.3", "10.0.03"],
            flag: "10.0.0.3",
            placeholder: "e.g., 10.0.0.10",
            hint: `Check out the new 'ARP-spoof-WARNING' logs <span class="has-text-weight-bold">or</span> some of the alarms themselves. Remember, there are two targets and one of them is plc1 with IP address 10.0.0.1`,

            isTerminalTask: false,

            triesLeft: 3,
            wrongTry: false,
            rightTry: false,
            terminalData: {}
        },
        {
            level: 3,
            responseActionID: "Flag 4",
            responseActionInstruction: `<span>&#62;</span><span>&#62;</span> Identify the host acting as the MitM.`,
            flagInstruction: `Submit this
<span class="has-tooltip-arrow has-tooltip-multiline has-tooltip-top" 
data-tooltip="A host can be identified by its IP address or its name.">
    <span class="has-text-link-dark has-text-weight-bold">
        host's name:
    </span>
</span>`,
            flagVariants: ["work-station", "10.0.0.5", "workstation"],
            flag: "work-station (10.0.0.5)",
            placeholder: "enter host name here ..",
            hint: `Remember, the attacker <span class="has-text-weight-bold">replaces their MAC address</span> with that of the target.`,

            isTerminalTask: false,

            triesLeft: 3,
            wrongTry: false,
            rightTry: false,
            terminalData: {}
        },

    ]
}

export default Unit2IdentTasks;