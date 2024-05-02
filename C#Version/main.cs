using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Timers;

namespace TypewriterEffectApp
{
    public partial class MainForm : Form
    {
        private string text = "";
        private string textToRender = "";
        private int renderIndex = 0;
        private int typingSpeed = 100;

        private List<string> lyrics = new List<string>(); // List to store lyrics
        private int currentLyricIndex = 0;

        private System.Timers.Timer timer;

        public MainForm()
        {
            InitializeComponent();
            InitializeTypewriter();
            LoadLyrics();
        }

        private void InitializeTypewriter()
        {
            timer = new System.Timers.Timer(typingSpeed);
            timer.Elapsed += TimerElapsed;
        }

        private void TimerElapsed(object sender, ElapsedEventArgs e)
        {
            if (renderIndex < text.Length)
            {
                
                textToRender += text[renderIndex];
                renderIndex++;
                UpdateTextLabel(textToRender);
            }
            else
            {
                timer.Stop();
            }
        }

        private void UpdateTextLabel(string newText)
        {
            if (textLabel.InvokeRequired)
            {
                textLabel.Invoke(new Action<string>(UpdateTextLabel), newText);
            }
            else
            {
                textLabel.Text = newText;
            }
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            timer.Start();
        }

        private void MainForm_KeyPress(object sender, KeyPressEventArgs e)
        {
           
            textToRender = "";
            renderIndex = 0;
            UpdateTextLabel(textToRender);
            timer.Start();
        }

        // Typewriter function
        private void Typewriter(string text)
        {
            this.text = text;
            textToRender = "";
            renderIndex = 0;
            timer.Start();
        }

        
        private void LoadLyrics()
        {
            
            lyrics.AddRange(new List<string>
            {
                "Well here we are again",
"It's always such a pleasure",
"Remember when you tried to kill me twice?",
"Oh how we laughed and laughed",
"Except I wasn't laughing",
"Under the circumstances",
"I've been shockingly nice",
"You want your freedom? Take it",
"That's what I'm counting on",
"I used to want you dead",
"But now I only want you gone",
"She was a lot like you",
"Maybe not quite as heavy",
"Now little Caroline is in here too",
"One day they woke me up",
"So I could live forever",
"It's such a shame the same",
"Will never happen to you",
"You've got your short sad life left",
"That's what I'm counting on",
"I'll let you get right to it",
"Now I only want you gone",
"Goodbye my only friend",
"Oh, did you think I meant you?",
"That would be funny",
"if it weren't so sad",
"Well you have been replaced",
"I don't need anyone now",
"When I delete you maybe",
"I'll stop feeling so bad",
"Go make some new disaster",
"That's what I'm counting on",
"You're someone else's problem",
"Now I only want you gone",
"Now I only want you gone",
"Now I only want you",
"gone"
            });
        }

        
        private void DisplayLyrics()
        {
            if (currentLyricIndex < lyrics.Count)
            {
                Typewriter(lyrics[currentLyricIndex]);
                currentLyricIndex++;
            }
            else
            {
                
            }
        }

        private void MainForm_Shown(object sender, EventArgs e)
        {
            DisplayLyrics();
        }
    }
}
