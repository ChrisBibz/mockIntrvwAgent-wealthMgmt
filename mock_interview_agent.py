
class MockInterviewAgent:
    def __init__(self):
        self.interview_data = [
            {
                "question": "Why do you want this job?",
                "response": "I am interested in how the variety of financial vehicles that people use to grow, maintain, and distribute wealth. I feel like educating people about methods of avoiding debt, increasing wealth, and generating stability for future generations or philanthropic pursuits is meaningful work. Your firm is a leader in the industry and I'd like to contribute my skills, gain experience, and build my career in such a place.",
                "follow_up": "Can you elaborate on how your skills and experiences align with the goals of our firm and the role you are applying for?"
            },
            {
                "question": "Can you elaborate on how your skills and experiences align with the goals of our firm and the role you are applying for?",
                "response": "I know that your firm believes in helping individuals and families plan for a broad range of goals. I appreciate that you work with clients of all backgrounds, income levels, and stages of their wealth journey. As an associate financial advisor who focused their undergraduate studies, internships, volunteer opportunities, and extracurricular activities on economics, geopolitics, global financial markets, alternative investments, and retirement planning, I feel well-qualified to help my peers and senior staff with their daily tasks as I learn the industry.",
                "follow_up": "Can you provide an example of a project or experience from your internships or volunteer opportunities that you believe has prepared you well for this role?"
            },
            {
                "question": "Can you provide an example of a project or experience from your internships or volunteer opportunities that you believe has prepared you well for this role?",
                "response": "I was part of a monthly financial clinic where senior community members could come for financial and estate planning advice, small business accounting assistance, and tax preparation services. Over a 12 month period, I assisted 40 people in those areas. My exposure to a variety of client personalities and financial circumstances helped me develop the interpersonal skills required to build and maintain trustworthy customer relationships and create strategies to improve each client's financial outcomes whether that meant reducing debt, preserving wealth, limiting tax exposure, or increasing profits.",
                "follow_up": "How did you handle a particularly challenging situation or client during your time at the financial clinic, and what did you learn from that experience?"
            },
            {
                "question": "How did you handle a particularly challenging situation or client during your time at the financial clinic, and what did you learn from that experience?",
                "response": "There was one particular client who had not paid taxes for six years. His personal belief was that he was a sovereign citizen; not beholden to any government and not responsible for paying taxes. Of course, the IRS and federal government disagreed and, after many letters and requests for filing, levied a large back tax bill. I had to learn to listen to this client's experience without judging it from my position. Initially, trying to convince him of the validity of paying taxes raised his defenses and activated negative emotions. Upon realizing that, I altered my approach to focus on the fact that we are solving a math problem and the better and more quickly we arrive at a solution, the sooner the problem goes away. After that, I showed him how the IRS calculated the tax bill so that he felt less taken advantage of. Then, I showed him how to arrange a payment plan with the IRS and how we could rebalance some of his existing assets to extinguish the debt.",
                "follow_up": "What did you learn from this experience that you believe will help you in a wealth management role, especially when dealing with clients who may have unconventional beliefs or challenging financial situations?"
            },
            {
                "question": "What did you learn from this experience that you believe will help you in a wealth management role, especially when dealing with clients who may have unconventional beliefs or challenging financial situations?",
                "response": "I learned that empathy is very important. Without that, the relationship may get off to a rocky start. My role is not to disagree or agree with their ideals or motivations, but to offer the best fiduciary advice I can for their situation. Their situation is not mine and its unfair to impose my beliefs upon my clients.",
                "follow_up": "How do you stay updated with the latest trends and developments in the financial industry to ensure that you are providing the most current and relevant advice to your clients?"
            },
            {
                "question": "How do you stay updated with the latest trends and developments in the financial industry to ensure that you are providing the most current and relevant advice to your clients?",
                "response": "I am a member of a professional organization for financial planners and wealth managers. I joined when I was a student and continue to receive their newsletters and attend their conferences. I also listen to several podcasts; one by a popular money manager, one by a successful trader, and one by a global economist. Each of their perspectives keeps me current on topics of those areas and listening to them helps me see how different components of the domestic and global financial industries interact to influence large and small clients' wealth journeys.",
                "follow_up": "How do you apply the insights and knowledge you gain from these sources to your work or interactions with clients? Can you provide an example of a time when this information helped you make a better decision or provide better advice?"
            },
            {
                "question": "How do you apply the insights and knowledge you gain from these sources to your work or interactions with clients? Can you provide an example of a time when this information helped you make a better decision or provide better advice?",
                "response": "Often, I immediately apply what I'm learning. Sometimes, I might learn about well-performing stocks on the Motley Fool podcast, evaluate them myself, and decide whether or not to add them to a model I've built. I think that following cryptocurrency throughout its rise in popularity helped several clients invest when it was a good fit and helped many clients avoid losing huge amounts by investing in memecoins and losing money to technology they didn't fully understand. Those clients had much better success with ETFs than they would have with crypto.",
                "follow_up": "How do you balance staying informed about emerging trends and technologies with ensuring that your advice remains grounded in sound financial principles? Can you provide an example of a time when you had to make a difficult decision between a trendy investment and a more traditional, stable option?"
            },
            {
                "question": "How do you balance staying informed about emerging trends and technologies with ensuring that your advice remains grounded in sound financial principles? Can you provide an example of a time when you had to make a difficult decision between a trendy investment and a more traditional, stable option?",
                "response": "I always remember and advise clients to remember that every investment should have sound fundamentals. If its an equity position, that means that the company is on sure-footing with a good balance sheet and sound management. Yes, there may be a hot stock that a customer wishes to pursue, and I will take time to hear what they hope to accomplish with that investment, but I will often redirect them to an investment vehicle that has a consistent return without as much risk. If they want to invest in a particular vehicle that they've read about or heard about from a friend, I make time to explain it and ask them to summarize their understanding. I don't believe that customers benefit from investment vehicles beyond their understanding. When they don't know how performance is calculated, the frequency of returns, management costs, etc, they can wind up unpleasantly surprised. By educating customers and suggesting sound, stable, consistent financial strategies, we all win.",
                "follow_up": "How do you handle situations where a client insists on pursuing a high-risk investment despite your advice? Can you provide an example of how you managed such a scenario and the outcome?"
            },
            {
                "question": "How do you handle situations where a client insists on pursuing a high-risk investment despite your advice? Can you provide an example of how you managed such a scenario and the outcome?",
                "response": "In those circumstances, I remember to see it from their perspective. If I've offered my advice and we have discussed the risk and benefits, they have the freedom to make their own choices and I must respect that. Sometimes it pays off for the customer and I learn to pay attention to a strategy that I might have previously discounted or ignored. When it doesn't pay off, I remember to have empathy with the customer and strategize to mitigate the loss. I definitely try to help them look forward instead of reminding them about the consequences of their choice. They already know that. In those instances, they're looking for hope, support, and guidance; not shame and judgment.",
                "follow_up": "How do you ensure that you maintain a balance between respecting clients' decisions and fulfilling your fiduciary duty to provide sound financial advice? Can you provide an example of a time when you had to navigate this balance?"
            }
        ]

    def conduct_interview(self):
        print("Welcome to the mock interview for an entry-level position at our wealth management firm.\n")
        for i, item in enumerate(self.interview_data):
            print(f"Question {i+1}: {item['question']}")
            print(f"Sample Response: {item['response']}")
            print(f"Follow-up Question: {item['follow_up']}\n")
        print("Thank you for participating in the mock interview. We hope this helps you prepare for your real interview.")

# Run the agent
if __name__ == "__main__":
    agent = MockInterviewAgent()
    agent.conduct_interview()
