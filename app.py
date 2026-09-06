import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="VLSI Interview Preparation Bot",
    page_icon="🧠",
    layout="centered"
)

# ---------------- DIGITAL ELECTRONICS QUESTIONS ----------------

digital_questions = [
    {
        "question": "Which logic gate produces HIGH output only when all inputs are HIGH?",
        "options": ["OR", "AND", "XOR", "NOT"],
        "answer": "AND",
        "explanation": "An AND gate gives HIGH output only when all of its inputs are HIGH."
    },
    {
        "question": "How many inputs does a NOT gate have?",
        "options": ["1", "2", "3", "4"],
        "answer": "1",
        "explanation": "A NOT gate has one input and produces the opposite output."
    },
    {
        "question": "Which gate is known as an inverter?",
        "options": ["AND", "OR", "NOT", "XOR"],
        "answer": "NOT",
        "explanation": "A NOT gate is also called an inverter because it reverses the input."
    },
    {
        "question": "Which logic gate produces HIGH output when any one of its inputs is HIGH?",
        "options": ["AND", "OR", "NOT", "NAND"],
        "answer": "OR",
        "explanation": "An OR gate produces HIGH output when at least one input is HIGH."
    },
    {
        "question": "What is the output of an AND gate when both inputs are 1?",
        "options": ["0", "1", "Undefined", "None"],
        "answer": "1",
        "explanation": "For an AND gate, 1 AND 1 gives 1."
    },
    {
        "question": "Which gate is called a universal gate?",
        "options": ["AND", "OR", "NAND", "XOR"],
        "answer": "NAND",
        "explanation": "NAND is a universal gate because basic logic gates can be implemented using NAND gates."
    },
    {
        "question": "Which other gate is a universal gate?",
        "options": ["NOR", "AND", "XOR", "NOT"],
        "answer": "NOR",
        "explanation": "NOR is also a universal gate and can be used to implement basic logic gates."
    },
    {
        "question": "What is the binary value of decimal 5?",
        "options": ["100", "101", "110", "111"],
        "answer": "101",
        "explanation": "Decimal 5 is represented as 101 in binary."
    },
    {
        "question": "A flip-flop can store how many bits?",
        "options": ["1 bit", "2 bits", "4 bits", "8 bits"],
        "answer": "1 bit",
        "explanation": "A flip-flop is a one-bit storage element."
    },
    {
        "question": "Which circuit is used to select one input from multiple inputs?",
        "options": ["Decoder", "Encoder", "Multiplexer", "Counter"],
        "answer": "Multiplexer",
        "explanation": "A multiplexer selects one input from multiple inputs and sends it to the output."
    }
]

# ---------------- VERILOG HDL QUESTIONS ----------------

verilog_questions = [
    {
        "question": "Which keyword is used to define a module in Verilog?",
        "options": ["module", "design", "entity", "block"],
        "answer": "module",
        "explanation": "The 'module' keyword is used to define a Verilog module."
    },
    {
        "question": "Which keyword is used for continuous assignment in Verilog?",
        "options": ["always", "assign", "continuous", "wire"],
        "answer": "assign",
        "explanation": "The 'assign' keyword is used for continuous assignment, commonly with nets such as wire."
    },
    {
        "question": "Which data type represents a physical connection between hardware elements?",
        "options": ["reg", "wire", "integer", "real"],
        "answer": "wire",
        "explanation": "A wire represents a connection between components and is commonly driven by continuous assignments or module outputs."
    },
    {
        "question": "Which block is commonly used to describe procedural behavior?",
        "options": ["assign", "always", "module", "wire"],
        "answer": "always",
        "explanation": "The always block is used to describe procedural behavior in Verilog."
    },
    {
        "question": "Which assignment operator is commonly used for blocking assignment?",
        "options": ["<=", "=", "==", "!="],
        "answer": "=",
        "explanation": "The '=' operator is used for blocking assignment."
    },
    {
        "question": "Which assignment operator is commonly used for non-blocking assignment?",
        "options": ["=", "<=", "==", "=>"],
        "answer": "<=",
        "explanation": "The '<=' operator is used for non-blocking assignment and is commonly used in sequential logic."
    },
    {
        "question": "Which construct is commonly used to describe multiple conditional choices?",
        "options": ["case", "wire", "module", "assign"],
        "answer": "case",
        "explanation": "The case statement is useful when selecting between multiple possible conditions or values."
    },
    {
        "question": "What does HDL stand for?",
        "options": [
            "Hardware Design Language",
            "Hardware Description Language",
            "High Data Language",
            "Hardware Digital Logic"
        ],
        "answer": "Hardware Description Language",
        "explanation": "HDL stands for Hardware Description Language. Verilog is an HDL used to describe digital hardware."
    },
    {
        "question": "Which statement is generally preferred for flip-flop logic?",
        "options": [
            "always @(posedge clk)",
            "assign",
            "wire",
            "initial only"
        ],
        "answer": "always @(posedge clk)",
        "explanation": "A clocked always block using a positive clock edge is commonly used to describe flip-flop-based sequential logic."
    },
    {
        "question": "Which of these is a Verilog logical operator?",
        "options": ["&&", "++", "::", "**"],
        "answer": "&&",
        "explanation": "The && operator is the logical AND operator in Verilog."
    }
]
# ---------------- SYSTEMVERILOG QUESTIONS ----------------

systemverilog_questions = [
    {
        "question": "Which SystemVerilog data type can be used instead of reg in most RTL designs?",
        "options": ["logic", "wire", "integer", "real"],
        "answer": "logic",
        "explanation": "SystemVerilog introduced the logic data type, which is commonly used for variables in RTL designs."
    },
    {
        "question": "Which SystemVerilog construct is specifically used to describe combinational logic?",
        "options": ["always_comb", "always_ff", "always_latch", "initial"],
        "answer": "always_comb",
        "explanation": "always_comb is designed for describing combinational logic."
    },
    {
        "question": "Which SystemVerilog construct is commonly used for flip-flop based sequential logic?",
        "options": ["always_comb", "always_ff", "always_latch", "assign"],
        "answer": "always_ff",
        "explanation": "always_ff is used to describe sequential logic such as flip-flops."
    },
    {
        "question": "Which SystemVerilog construct is used to describe latch behavior?",
        "options": ["always_ff", "always_comb", "always_latch", "assign"],
        "answer": "always_latch",
        "explanation": "always_latch is specifically intended for describing latch-based logic."
    },
    {
        "question": "Which keyword is used to define an enumeration in SystemVerilog?",
        "options": ["enum", "typedef", "struct", "class"],
        "answer": "enum",
        "explanation": "The enum keyword is used to define an enumeration containing a set of named values."
    },
    {
        "question": "Which keyword can create a user-defined type in SystemVerilog?",
        "options": ["typedef", "define", "type", "custom"],
        "answer": "typedef",
        "explanation": "typedef allows a new name to be given to an existing or user-defined data type."
    },
    {
        "question": "Which SystemVerilog feature groups different data types into one composite data structure?",
        "options": ["enum", "struct", "interface", "package"],
        "answer": "struct",
        "explanation": "A struct groups multiple data members, potentially of different types, into one composite type."
    },
    {
        "question": "What is the main purpose of an interface in SystemVerilog?",
        "options": [
            "To connect and group signals between modules",
            "To replace all modules",
            "To store simulation results",
            "To create clock signals automatically"
        ],
        "answer": "To connect and group signals between modules",
        "explanation": "An interface groups related signals and can simplify communication between modules and verification components."
    },
    {
        "question": "Which SystemVerilog feature is commonly used to check design behavior during simulation?",
        "options": ["Assertions", "Packages", "Enums", "Structs"],
        "answer": "Assertions",
        "explanation": "SystemVerilog assertions are used to check whether specified design properties hold during simulation."
    },
    {
        "question": "SystemVerilog is primarily an extension of which language?",
        "options": ["VHDL", "Verilog", "Python", "C++"],
        "answer": "Verilog",
        "explanation": "SystemVerilog extends Verilog with additional RTL, verification, and programming features."
    }
]
# ---------------- CMOS FUNDAMENTALS QUESTIONS ----------------

cmos_questions = [
    {
        "question": "What is the full form of CMOS?",
        "options": [
            "Complementary Metal Oxide Semiconductor",
            "Common Metal Oxide Semiconductor",
            "Complementary Metal Output System",
            "Current Mode Operating System"
        ],
        "answer": "Complementary Metal Oxide Semiconductor",
        "explanation": "CMOS stands for Complementary Metal Oxide Semiconductor."
    },
    {
        "question": "Which two types of MOSFETs are used in CMOS logic?",
        "options": [
            "NMOS and PMOS",
            "BJT and JFET",
            "NPN and PNP",
            "JFET and CMOS"
        ],
        "answer": "NMOS and PMOS",
        "explanation": "CMOS logic uses complementary NMOS and PMOS transistors."
    },
    {
        "question": "In a CMOS inverter, which transistor is connected to VDD?",
        "options": ["NMOS", "PMOS", "Both", "Neither"],
        "answer": "PMOS",
        "explanation": "The PMOS transistor forms the pull-up network and is connected to VDD."
    },
    {
        "question": "In a CMOS inverter, which transistor is connected to ground?",
        "options": ["PMOS", "NMOS", "Both", "Neither"],
        "answer": "NMOS",
        "explanation": "The NMOS transistor forms the pull-down network and is connected to ground."
    },
    {
        "question": "What is one major advantage of CMOS logic?",
        "options": [
            "Low static power consumption",
            "Very high static power",
            "No transistors are required",
            "It only works with analog signals"
        ],
        "answer": "Low static power consumption",
        "explanation": "CMOS circuits have very low static power consumption because ideally there is no direct DC path from VDD to ground in steady states."
    },
    {
        "question": "What does VDD generally represent in CMOS circuits?",
        "options": [
            "Positive supply voltage",
            "Ground voltage",
            "Output voltage only",
            "Input signal"
        ],
        "answer": "Positive supply voltage",
        "explanation": "VDD generally denotes the positive power supply in CMOS circuits."
    },
    {
        "question": "What does the NMOS transistor primarily provide in CMOS logic?",
        "options": [
            "Pull-down path",
            "Pull-up path",
            "Clock generation",
            "Memory storage"
        ],
        "answer": "Pull-down path",
        "explanation": "NMOS transistors form the pull-down network that connects the output toward ground."
    },
    {
        "question": "What does the PMOS transistor primarily provide in CMOS logic?",
        "options": [
            "Pull-up path",
            "Pull-down path",
            "Ground connection only",
            "Clock generation"
        ],
        "answer": "Pull-up path",
        "explanation": "PMOS transistors form the pull-up network that connects the output toward VDD."
    },
    {
        "question": "What happens to the output of a CMOS inverter when the input is HIGH?",
        "options": ["Output is HIGH", "Output is LOW", "Output becomes undefined", "Output becomes analog"],
        "answer": "Output is LOW",
        "explanation": "When the input is HIGH, NMOS turns ON and PMOS turns OFF, pulling the output LOW."
    },
    {
        "question": "What happens to the output of a CMOS inverter when the input is LOW?",
        "options": ["Output is LOW", "Output is HIGH", "Output becomes undefined", "Both transistors turn ON"],
        "answer": "Output is HIGH",
        "explanation": "When the input is LOW, PMOS turns ON and NMOS turns OFF, pulling the output HIGH."
    }
]
# ---------------- DESIGN VERIFICATION QUESTIONS ----------------

dv_questions = [
    {
        "question": "What is the primary purpose of design verification?",
        "options": [
            "To check whether the design behaves according to its specification",
            "To manufacture the chip",
            "To increase the clock frequency automatically",
            "To create the PCB"
        ],
        "answer": "To check whether the design behaves according to its specification",
        "explanation": "Design verification checks whether the implemented design behaves as expected according to its specification."
    },
    {
        "question": "What does RTL stand for?",
        "options": [
            "Register Transfer Level",
            "Real Time Logic",
            "Register Timing Logic",
            "Random Transfer Language"
        ],
        "answer": "Register Transfer Level",
        "explanation": "RTL stands for Register Transfer Level and describes digital hardware in terms of registers and the logic between them."
    },
    {
        "question": "What is a testbench?",
        "options": [
            "A simulation environment used to verify a design",
            "A physical testing machine only",
            "A synthesis tool",
            "A type of FPGA"
        ],
        "answer": "A simulation environment used to verify a design",
        "explanation": "A testbench provides stimulus to the design under test and observes its outputs during simulation."
    },
    {
        "question": "What does DUT stand for in verification?",
        "options": [
            "Design Under Test",
            "Data Under Transfer",
            "Digital Utility Tool",
            "Design Utility Technology"
        ],
        "answer": "Design Under Test",
        "explanation": "DUT stands for Design Under Test—the design or module being verified."
    },
    {
        "question": "What is functional verification mainly concerned with?",
        "options": [
            "Checking whether the design performs its intended functions",
            "Checking only transistor size",
            "Manufacturing the chip",
            "Checking PCB dimensions"
        ],
        "answer": "Checking whether the design performs its intended functions",
        "explanation": "Functional verification checks whether the design produces the expected behavior for different input conditions."
    },
    {
        "question": "What is a test stimulus?",
        "options": [
            "Input applied to the DUT during verification",
            "The final chip package",
            "A clock generation circuit only",
            "A synthesis report"
        ],
        "answer": "Input applied to the DUT during verification",
        "explanation": "Stimulus is the input data or sequence applied to the DUT to test its behavior."
    },
    {
        "question": "What is coverage in design verification?",
        "options": [
            "A measure of how much of the design or verification space has been exercised",
            "The physical area of a chip",
            "The number of transistors on a chip",
            "The power supply voltage"
        ],
        "answer": "A measure of how much of the design or verification space has been exercised",
        "explanation": "Coverage helps measure how thoroughly the design and its behaviors have been exercised during verification."
    },
    {
        "question": "Which language is widely used for hardware verification along with Verilog/SystemVerilog?",
        "options": [
            "SystemVerilog",
            "HTML",
            "SQL",
            "CSS"
        ],
        "answer": "SystemVerilog",
        "explanation": "SystemVerilog provides extensive RTL and verification features and is widely used for modern hardware verification."
    },
    {
        "question": "What is a directed test?",
        "options": [
            "A test specifically designed for a particular scenario",
            "A test generated randomly only",
            "A synthesis command",
            "A physical manufacturing test"
        ],
        "answer": "A test specifically designed for a particular scenario",
        "explanation": "A directed test is intentionally written to exercise a particular behavior or scenario of the DUT."
    },
    {
        "question": "Why are corner cases important in verification?",
        "options": [
            "They help find bugs in unusual or boundary conditions",
            "They reduce the number of tests automatically",
            "They are only used during chip packaging",
            "They increase transistor count"
        ],
        "answer": "They help find bugs in unusual or boundary conditions",
        "explanation": "Corner cases test unusual, extreme, or boundary conditions where hidden design bugs may appear."
    }
]

# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "topic" not in st.session_state:
    st.session_state.topic = None

if "question_number" not in st.session_state:
    st.session_state.question_number = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "last_answer" not in st.session_state:
    st.session_state.last_answer = None


# ---------------- RESET QUIZ ----------------

def start_quiz(topic):
    st.session_state.topic = topic
    st.session_state.page = "quiz"
    st.session_state.question_number = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.last_answer = None
    st.rerun()


# ---------------- HOME PAGE ----------------

if st.session_state.page == "home":

    st.title("🧠 VLSI Interview Preparation Bot")

    st.write(
        "Welcome! Practice VLSI concepts through topic-wise MCQs."
    )

    st.divider()

    st.subheader("📚 Select Your Topic")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🔵 Digital Electronics",
            use_container_width=True
        ):
            start_quiz("Digital Electronics")

        if st.button(
            "🟢 Verilog HDL",
            use_container_width=True
        ):
            start_quiz("Verilog HDL")

        if st.button(
            "🟣 SystemVerilog",
            use_container_width=True
        ):
            start_quiz("SystemVerilog")

    with col2:

        if st.button(
           "🟠 CMOS Fundamentals",
           use_container_width=True
      ):
           start_quiz("CMOS Fundamentals")

        if st.button(
          "🔴 Design Verification",
          use_container_width=True
        ):
          start_quiz("Design Verification")
    st.divider()

    st.caption("VLSI Interview Preparation Bot • Basic Version")


# ---------------- QUIZ PAGE ----------------

elif st.session_state.page == "quiz":

    # Select question set

    if st.session_state.topic == "Digital Electronics":
        questions = digital_questions
        emoji = "🔵"

    elif st.session_state.topic == "Verilog HDL":
        questions = verilog_questions
        emoji = "🟢"

    elif st.session_state.topic == "SystemVerilog":
        questions = systemverilog_questions
        emoji = "🟣"

    elif st.session_state.topic == "CMOS Fundamentals":
        questions = cmos_questions
        emoji = "🟠"

    elif st.session_state.topic == "Design Verification":
        questions = dv_questions
        emoji = "🔴"

    else:
        questions = []

    question_index = st.session_state.question_number

    # ---------------- FINAL RESULT ----------------

    if question_index >= len(questions):

        st.title("🎉 Test Completed!")

        st.divider()

        st.subheader(
            f"Your Score: {st.session_state.score} / {len(questions)}"
        )

        percentage = (
            st.session_state.score / len(questions)
        ) * 100

        st.write(f"### 📊 Percentage: {percentage:.0f}%")

        if percentage >= 80:
            st.success("Excellent! 🔥 Keep it up!")

        elif percentage >= 50:
            st.info("Good job! 👍 Keep practicing.")

        else:
            st.warning("Keep practicing. You can improve! 💪")

        st.divider()

        if st.button(
            "🔄 Practice Again",
            use_container_width=True
        ):

            start_quiz(st.session_state.topic)

        if st.button(
            "🏠 Back to Topics",
            use_container_width=True
        ):

            st.session_state.page = "home"
            st.session_state.topic = None
            st.session_state.question_number = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.last_answer = None
            st.rerun()

    # ---------------- QUESTION ----------------

    else:

        question = questions[question_index]

        st.title(
            f"{emoji} {st.session_state.topic} Practice"
        )

        st.progress(
            (question_index + 1) / len(questions)
        )

        st.write(
            f"### Question {question_index + 1} of {len(questions)}"
        )

        st.write(
            f"**{question['question']}**"
        )

        # ---------------- BEFORE ANSWER ----------------

        if not st.session_state.answered:

            selected = st.radio(
                "Select your answer:",
                question["options"],
                key=f"{st.session_state.topic}_{question_index}"
            )

            st.divider()

            if st.button(
                "✅ Submit Answer",
                use_container_width=True
            ):

                st.session_state.last_answer = selected
                st.session_state.answered = True

                if selected == question["answer"]:
                    st.session_state.score += 1

                st.rerun()

        # ---------------- AFTER ANSWER ----------------

        else:

            selected = st.session_state.last_answer

            if selected == question["answer"]:

                st.success("✅ Correct Answer!")

            else:

                st.error("❌ Wrong Answer!")

                st.write(
                    f"**Correct Answer:** {question['answer']}"
                )

            st.info(
                f"💡 **Explanation:** {question['explanation']}"
            )

            st.divider()

            if st.button(
                "➡️ Next Question",
                use_container_width=True
            ):

                st.session_state.question_number += 1
                st.session_state.answered = False
                st.session_state.last_answer = None

                st.rerun()

            if st.button(
                "🏠 Back to Topics",
                use_container_width=True
            ):

                st.session_state.page = "home"
                st.session_state.topic = None
                st.session_state.question_number = 0
                st.session_state.score = 0
                st.session_state.answered = False
                st.session_state.last_answer = None

                st.rerun()